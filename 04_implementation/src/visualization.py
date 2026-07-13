"""Funciones de visualización para el proyecto de manifold embeddings.

Universidad Nacional Mayor de San Marcos
Doctorado en DeepTech — IA y Tecnologías Emergentes
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional


def plot_embedding_2d(
    X_embedded: np.ndarray,
    y: np.ndarray,
    title: str = 'Embedding 2D',
    ax: Optional[plt.Axes] = None,
    cmap: str = 'tab10',
    s: int = 15,
    alpha: float = 0.7
) -> plt.Axes:
    """Visualiza un embedding 2D coloreado por etiquetas."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    scatter = ax.scatter(
        X_embedded[:, 0], X_embedded[:, 1],
        c=y, cmap=cmap, s=s, alpha=alpha, edgecolors='none'
    )
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Componente 1', fontsize=12)
    ax.set_ylabel('Componente 2', fontsize=12)
    plt.colorbar(scatter, ax=ax, shrink=0.8)
    return ax


def plot_embedding_3d(
    X: np.ndarray,
    y: np.ndarray,
    title: str = 'Datos 3D',
    figsize: tuple = (10, 8)
) -> plt.Figure:
    """Visualiza datos en 3D."""
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis', s=10, alpha=0.6)
    ax.set_title(title, fontsize=14, fontweight='bold')
    return fig


def plot_metric_vs_k(
    results_df: pd.DataFrame,
    metric_name: str,
    methods: list[str] = ['isomap', 'lle'],
    ax: Optional[plt.Axes] = None,
    title: Optional[str] = None
) -> plt.Axes:
    """Grafica una métrica vs k para múltiples métodos."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    for method in methods:
        data = results_df[results_df['method'] == method]
        ax.plot(data['k'], data[metric_name], 'o-', label=method.upper(),
                linewidth=2, markersize=6)
    ax.set_xlabel('k (número de vecinos)', fontsize=12)
    ax.set_ylabel(metric_name.replace('_', ' ').title(), fontsize=12)
    ax.set_title(title or f'{metric_name.replace("_", " ").title()} vs k',
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    return ax


def plot_all_metrics_comparison(
    results_df: pd.DataFrame,
    k_values: list[int],
    dataset_name: str = 'Dataset'
) -> plt.Figure:
    """Crea un grid de plots con todas las métricas vs k."""
    metrics = [
        'trustworthiness', 'continuity', 'stress',
        'residual_variance', 'classification_accuracy_knn',
        'classification_accuracy_svm', 'silhouette_score'
    ]
    fig, axes = plt.subplots(3, 3, figsize=(18, 14))
    fig.suptitle(f'Comparación de Métricas — {dataset_name}',
                 fontsize=16, fontweight='bold')
    for idx, metric in enumerate(metrics):
        if metric in results_df.columns:
            ax = axes[idx // 3, idx % 3]
            plot_metric_vs_k(results_df, metric, ax=ax)
    for idx in range(len(metrics), 9):
        axes[idx // 3, idx % 3].set_visible(False)
    plt.tight_layout()
    return fig


def plot_embedding_grid(
    embeddings_dict: dict,
    y: np.ndarray,
    k_values: list[int],
    methods: list[str] = ['isomap', 'lle']
) -> plt.Figure:
    """Crea un grid de embeddings: filas = métodos, columnas = k."""
    n_methods = len(methods)
    n_k = len(k_values)
    fig, axes = plt.subplots(n_methods, n_k, figsize=(4 * n_k, 4 * n_methods))
    fig.suptitle('Embeddings 2D: Efecto de k', fontsize=16, fontweight='bold', y=1.02)
    for i, method in enumerate(methods):
        for j, k in enumerate(k_values):
            ax = axes[i, j] if n_methods > 1 else axes[j]
            key = (method, k)
            if key in embeddings_dict:
                emb = embeddings_dict[key]
                ax.scatter(emb[:, 0], emb[:, 1], c=y, cmap='tab10', s=10, alpha=0.6)
            ax.set_title(f'{method.upper()}, k={k}', fontsize=11)
            ax.set_xticks([])
            ax.set_yticks([])
    plt.tight_layout()
    return fig


def save_figure(
    fig: plt.Figure,
    name: str,
    output_dir: str = '../../07_visualizations/figures',
    dpi: int = 300,
    formats: list[str] = ['png']
) -> None:
    """Guarda una figura en el directorio de visualizaciones."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    for fmt in formats:
        filepath = output_path / f'{name}.{fmt}'
        fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
        print(f'Figura guardada: {filepath}')
