<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 🔢 Guía: Mathematical Background

## ¿Qué debe contener esta carpeta?

El archivo `mathematical_background.md` con el fundamento matemático completo.

## Temas que DEBEN cubrirse

### 1. Manifold Learning — Fundamentos
- Definición de variedad (manifold)
- Hipótesis del manifold (manifold hypothesis)
- Reducción de dimensionalidad no lineal vs lineal (PCA como baseline)

### 2. Isomap (Isometric Mapping)
- Algoritmo paso a paso
- Construcción del grafo de k-vecinos más cercanos
- Cálculo de distancias geodésicas (Dijkstra / Floyd-Warshall)
- Multi-Dimensional Scaling (MDS) clásico
- Eigenvalue decomposition
- Complejidad computacional
- Rol del parámetro k

### 3. LLE (Locally Linear Embedding)
- Algoritmo paso a paso
- Selección de vecinos (k-nearest neighbors)
- Cálculo de pesos de reconstrucción (minimización de error)
- Embedding: eigenvalue problem con matriz sparse
- Variantes: Modified LLE, Hessian LLE, LTSA
- Complejidad computacional
- Rol del parámetro k

### 4. Métricas de Evaluación
- **Trustworthiness** — fórmula y significado
- **Continuity** — fórmula y significado
- **Residual Variance** — para Isomap
- **Reconstruction Error** — para LLE
- **Stress** (Kruskal)
- **Classification Accuracy** — KNN, SVM en espacio embebido
- **Silhouette Score** — coherencia de clusters

### 5. Análisis de Sensibilidad
- Cómo varía la conectividad del grafo con k
- Trade-off entre ruido local y estructura global
- Grafos desconectados cuando k es muy pequeño
- Cortocircuitos cuando k es muy grande

## Notación Matemática

Usar LaTeX en markdown:
- $\mathbf{X} \in \mathbb{R}^{n \times D}$ — datos originales
- $\mathbf{Y} \in \mathbb{R}^{n \times d}$ — embedding (d << D)
- $k$ — número de vecinos cercanos
- $d_G(i,j)$ — distancia geodésica entre puntos i, j
- $W$ — matriz de pesos

## Estado
- **Responsable principal:** Christian Chiroque Ruiz
- **Revisores:** Elmer Gomez, Jean Pierre Tincopa
- **Fecha límite borrador:** 16 de julio de 2026
- **Fecha límite final:** 20 de julio de 2026
