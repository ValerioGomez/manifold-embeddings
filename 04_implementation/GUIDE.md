<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 💻 Guía: Implementation

## ¿Qué debe contener esta carpeta?

### notebooks/
Jupyter Notebooks bien documentados:

| Notebook | Descripción | Responsable |
|---|---|---|
| 01_data_loading.ipynb | Carga y preprocesamiento de datos | Jean Pierre |
| 02_isomap_experiments.ipynb | Experimentos con Isomap variando k | Elmer |
| 03_lle_experiments.ipynb | Experimentos con LLE variando k | Christian |
| 04_comparison_analysis.ipynb | Análisis comparativo Isomap vs LLE | TODOS |
| 05_visualizations.ipynb | Visualizaciones finales | Jean Pierre |

### src/
Módulos Python reutilizables:

| Módulo | Descripción |
|---|---|
| data_loader.py | Funciones para cargar datasets (Swiss Roll, MNIST subset, Wine, etc.) |
| embeddings.py | Wrappers para Isomap y LLE con logging de métricas |
| metrics.py | Implementación de trustworthiness, continuity, stress, classification metrics |
| visualization.py | Funciones de visualización estandarizadas |
| utils.py | Utilidades generales |

### tests/
Tests unitarios para verificar implementaciones.

## Convenciones

- Python 3.10+
- Usar scikit-learn para Isomap y LLE base
- Cada notebook debe ser ejecutable de principio a fin sin errores
- Usar random seeds para reproducibilidad (seed=42)
- Cada celda de código debe tener una celda markdown explicativa arriba
- Los resultados intermedios se guardan en `05_experiments/results/`

## Datasets a Utilizar

### Sintético
- **Swiss Roll** (sklearn.datasets.make_swiss_roll, n=1500-2000)
- **S-Curve** (sklearn.datasets.make_s_curve, opcional)

### Real (elegir al menos uno)
- **MNIST Digits** (subset de 1000-2000 muestras, dígitos 0-5)
- **Wine Dataset** (sklearn.datasets.load_wine)
- **Breast Cancer** (sklearn.datasets.load_breast_cancer)
- **Olivetti Faces** (sklearn.datasets.fetch_olivetti_faces)

## Rango de k a Explorar
- k = [3, 5, 7, 10, 15, 20, 25, 30, 40, 50]
- Para cada k, computar TODAS las métricas
- Guardar resultados en formato CSV/pickle

## Estado
- **Responsable principal:** Jean Pierre Tincopa Flores
- **Fecha límite módulos base:** 17 de julio de 2026
- **Fecha límite notebooks:** 20 de julio de 2026
