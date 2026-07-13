<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 📈 Guía: Visualizations

## ¿Qué debe contener esta carpeta?

### figures/
Todas las figuras generadas por los experimentos.

## Visualizaciones Requeridas

### 1. Datos Originales
- [ ] Swiss Roll 3D con colores por posición
- [ ] Dataset real: distribución de features principales (PCA 2D como referencia)

### 2. Embeddings 2D
- [ ] Grid de embeddings: filas = métodos (Isomap, LLE), columnas = valores de k seleccionados (e.g., k=5, 10, 20, 40)
- [ ] Coloreados por clase/posición real

### 3. Métricas vs k
- [ ] Trustworthiness vs k (ambos métodos en el mismo plot)
- [ ] Continuity vs k
- [ ] Classification Accuracy vs k (KNN y SVM)
- [ ] Residual Variance / Reconstruction Error vs k
- [ ] Silhouette Score vs k
- [ ] Execution Time vs k

### 4. Comparación
- [ ] Heatmap de métricas (filas: k, columnas: métricas, separado por método)
- [ ] Radar/Spider chart comparando Isomap vs LLE para k óptimo
- [ ] Barplot del mejor rendimiento de cada método

### 5. Análisis Adicional
- [ ] Eigenvalue spectrum (para entender la dimensión intrínseca)
- [ ] Connectivity del grafo vs k (número de componentes conectadas)

## Convenciones de Estilo
- Fuente: 12pt para etiquetas, 14pt para títulos
- Colormap: tab10 para clases, viridis para continuous
- Figuras: 300 DPI para el informe
- Formato: PNG para notebooks, PDF para el informe
- Nombres: `{dataset}_{method}_{metric}_{k}.png`

## Estado
- **Responsable principal:** Jean Pierre Tincopa
- **Fecha límite:** 22 de julio de 2026
