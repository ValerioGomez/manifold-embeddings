"""Utilidades generales para el proyecto de manifold embeddings.

Universidad Nacional Mayor de San Marcos
Facultad de Ingeniería de Sistemas e Informática
Doctorado en DeepTech — IA y Tecnologías Emergentes
"""

import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Any

DEFAULT_SEED = 42

def set_random_seed(seed: int = DEFAULT_SEED) -> None:
    """Fija la semilla aleatoria para reproducibilidad en numpy y sklearn."""
    np.random.seed(seed)
    print(f'Random seed fijado: {seed}')

def setup_plotting_style() -> None:
    """Configura el estilo de los plots para los reportes y notebooks."""
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'figure.dpi': 150,
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'legend.fontsize': 11,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 16,
    })
    sns.set_theme(style='whitegrid', palette='deep')
    print('Estilo de visualización configurado.')

def save_results(
    results: Any,
    filepath: str,
    format: str = 'csv'
) -> None:
    """Guarda los resultados de las métricas en formato CSV o Pickle."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    if format == 'csv' and isinstance(results, pd.DataFrame):
        results.to_csv(filepath, index=False)
    elif format == 'pickle':
        with open(filepath, 'wb') as f:
            pickle.dump(results, f)
    else:
        raise ValueError(f'Formato no soportado o tipo de datos no coincide: {format}')
    print(f'Resultados guardados: {filepath}')

def load_results(filepath: str) -> Any:
    """Carga resultados previamente guardados (CSV o Pickle)."""
    path = Path(filepath)
    if path.suffix == '.csv':
        return pd.read_csv(filepath)
    elif path.suffix == '.pkl':
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError(f'Formato no reconocido: {path.suffix}')

def print_experiment_summary(results_df: pd.DataFrame) -> None:
    """Imprime un resumen formateado de los experimentos."""
    print('=' * 70)
    print('RESUMEN DE EXPERIMENTOS (MANIFOLD EMBEDDINGS)')
    print('=' * 70)

    for method in results_df['method'].unique():
        data = results_df[results_df['method'] == method]
        print(f"\n--- Método: {method.upper()} ---")
        print(f" Valores de k evaluados: {sorted(data['k'].unique())}")
        
        metrics = [
            'trustworthiness', 'continuity', 'stress',
            'classification_accuracy_knn', 'silhouette_score'
        ]
        for metric in metrics:
            if metric in data.columns:
                if metric in ['stress', 'residual_variance']:
                    best_idx = data[metric].idxmin()
                    action = "Menor"
                else:
                    best_idx = data[metric].idxmax()
                    action = "Mayor"
                best_k = data.loc[best_idx, 'k']
                best_val = data.loc[best_idx, metric]
                print(f"  {action} {metric}: {best_val:.4f} (obtenido con k={best_k})")
    print('=' * 70)
