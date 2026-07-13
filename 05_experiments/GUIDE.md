<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 🧪 Guía: Experiments

## ¿Qué debe contener esta carpeta?

### configs/
Archivos de configuración YAML para reproducibilidad.

### results/
Resultados de los experimentos en formato CSV y pickle.

## Diseño Experimental

### Variables

| Variable | Tipo | Valores |
|---|---|---|
| Método de embedding | Independiente | Isomap, LLE |
| Número de vecinos (k) | Independiente | 3, 5, 7, 10, 15, 20, 25, 30, 40, 50 |
| Dataset | Independiente | Swiss Roll, [Dataset Real] |
| Dimensión del embedding (d) | Controlada | 2 |
| Random seed | Controlada | 42 |
| Trustworthiness | Dependiente | [0, 1] |
| Continuity | Dependiente | [0, 1] |
| Classification Accuracy | Dependiente | [0, 1] |
| Residual Variance | Dependiente | [0, ∞) |
| Reconstruction Error | Dependiente | [0, ∞) |
| Silhouette Score | Dependiente | [-1, 1] |
| Execution Time | Dependiente | segundos |

### Matriz de Experimentos

Total de combinaciones: 2 métodos × 10 valores de k × 2 datasets = 40 experimentos

Cada experimento produce:
- Embedding 2D (para visualización)
- 7 métricas de evaluación
- Tiempo de ejecución

### Protocolo

1. Fijar random seed = 42
2. Cargar dataset
3. Para cada método (Isomap, LLE):
   a. Para cada k en [3, 5, 7, 10, 15, 20, 25, 30, 40, 50]:
      - Ejecutar embedding
      - Computar todas las métricas
      - Guardar embedding y métricas
      - Registrar tiempo de ejecución
4. Agregar resultados en DataFrame
5. Guardar en CSV

## Estructura de Resultados

CSV con columnas:
```
method, dataset, k, trustworthiness, continuity, stress, residual_variance, reconstruction_error, classification_accuracy_knn, classification_accuracy_svm, silhouette_score, execution_time_seconds
```

## Estado
- **Responsable Isomap:** Elmer Gomez Alcos
- **Responsable LLE:** Christian Chiroque Ruiz  
- **Integración:** Jean Pierre Tincopa
- **Fecha límite:** 20 de julio de 2026
