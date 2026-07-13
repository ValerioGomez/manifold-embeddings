<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# Fundamento Matemático: Isomap y LLE

**Responsable principal:** Christian Chiroque Ruiz
**Revisores:** Elmer Gomez Alcos, Jean Pierre Tincopa Flores

---

## 1. Manifold Learning — Fundamentos

### 1.1 Definición de Variedad (Manifold)

Una **variedad diferenciable** $\mathcal{M}$ de dimensión $d$ es un espacio topológico que es localmente homeomorfo a $\mathbb{R}^d$. Para cada punto $p \in \mathcal{M}$, existe un entorno abierto $U$ de $p$ y un homeomorfismo $\phi: U \rightarrow V \subseteq \mathbb{R}^d$.

### 1.2 Hipótesis del Manifold

La **hipótesis del manifold** establece que datos de alta dimensionalidad $\mathbf{X} \in \mathbb{R}^{n \times D}$ frecuentemente residen cerca de una variedad de baja dimensionalidad $\mathcal{M} \subset \mathbb{R}^D$, donde $\dim(\mathcal{M}) = d \ll D$.

### 1.3 Reducción de Dimensionalidad

**Objetivo:** Encontrar un mapeo $f: \mathbb{R}^D \rightarrow \mathbb{R}^d$ que preserve la estructura geométrica.

| Tipo | Método | Preserva |
|------|--------|----------|
| Lineal | PCA | Varianza global |
| No lineal | Isomap | Distancias geodésicas |
| No lineal | LLE | Geometría local |

---

## 2. Isomap (Isometric Feature Mapping)

**Referencia:** Tenenbaum, de Silva & Langford (2000), *Science*.

### 2.1 Algoritmo

**Entrada:** $\mathbf{X} = \{x_1, \ldots, x_n\} \subset \mathbb{R}^D$, parámetros $k$ (vecinos), $d$ (dimensión embedding).

**Paso 1: Grafo de k-vecinos**

Para cada $x_i$, identificar sus $k$ vecinos más cercanos:

$$d_E(x_i, x_j) = \|x_i - x_j\|_2$$

Construir $G = (V, E)$ donde $(x_i, x_j) \in E$ si $x_j \in \text{KNN}(x_i)$ o $x_i \in \text{KNN}(x_j)$.

**Paso 2: Distancias geodésicas**

$$d_G(x_i, x_j) = \min_{\text{path}(i \rightarrow j)} \sum_{(a,b) \in \text{path}} w(a, b)$$

Usando Dijkstra ($O(n^2 \log n)$) o Floyd-Warshall ($O(n^3)$).

**Paso 3: MDS Clásico (double centering)**

$$\mathbf{B} = -\frac{1}{2} \mathbf{H} \mathbf{D}_G^{(2)} \mathbf{H}$$

donde $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}_n\mathbf{1}_n^T$.

**Paso 4: Eigendecomposición**

$$\mathbf{B} = \mathbf{V} \boldsymbol{\Lambda} \mathbf{V}^T$$

**Paso 5: Coordenadas del embedding**

$$\mathbf{Y} = \boldsymbol{\Lambda}_d^{1/2} \mathbf{V}_d^T \in \mathbb{R}^{d \times n}$$

### 2.2 Rol del Parámetro k en Isomap

- **k muy pequeño:** Grafo puede quedar desconectado
- **k moderado:** Buena aproximación de distancias geodésicas
- **k muy grande:** Cortocircuitos que subestiman distancias geodésicas

### 2.3 Complejidad: $O(n^3)$

---

## 3. LLE (Locally Linear Embedding)

**Referencia:** Roweis & Saul (2000), *Science*.

### 3.1 Algoritmo

**Paso 1:** Encontrar $k$ vecinos más cercanos para cada $x_i$.

**Paso 2: Pesos de reconstrucción**

Minimizar:

$$\mathcal{E}(\mathbf{W}) = \sum_{i=1}^{n} \left\| x_i - \sum_{j \in \mathcal{N}_i} w_{ij} x_j \right\|^2$$

Sujeto a: $w_{ij} = 0$ si $x_j \notin \mathcal{N}_i$ y $\sum_j w_{ij} = 1$.

Solución mediante la **matriz de Gram local:**

$$G_{jl}^{(i)} = (x_i - x_{i_j})^T (x_i - x_{i_l})$$

**Paso 3: Embedding**

Minimizar:

$$\Phi(\mathbf{Y}) = \sum_{i=1}^{n} \left\| y_i - \sum_j w_{ij} y_j \right\|^2 = \text{tr}(\mathbf{Y}^T \mathbf{M} \mathbf{Y})$$

donde $\mathbf{M} = (\mathbf{I} - \mathbf{W})^T(\mathbf{I} - \mathbf{W})$.

Solución: eigenvectores de los $d$ eigenvalores más pequeños no nulos de $\mathbf{M}$.

### 3.2 Rol del Parámetro k en LLE

- **k muy pequeño:** Pesos inestables, sistema subdeterminado
- **k moderado:** Buena aproximación lineal local
- **k muy grande:** Aproximación lineal no válida

### 3.3 Complejidad: $O(Dn^2)$

---

## 4. Métricas de Evaluación

### 4.1 Trustworthiness

$$T(k) = 1 - \frac{2}{nk(2n - 3k - 1)} \sum_{i=1}^{n} \sum_{j \in \mathcal{U}_i^{(k)}} (r(i,j) - k)$$

Mide si el embedding no introduce falsos vecinos. $T(k) \in [0, 1]$, ideal $\geq 0.95$.

### 4.2 Continuity

$$C(k) = 1 - \frac{2}{nk(2n - 3k - 1)} \sum_{i=1}^{n} \sum_{j \in \mathcal{V}_i^{(k)}} (\hat{r}(i,j) - k)$$

Mide si el embedding no "rompe" vecindarios. $C(k) \in [0, 1]$, ideal $\geq 0.95$.

### 4.3 Kruskal Stress

$$\text{Stress} = \sqrt{\frac{\sum_{i<j}(d_{ij} - \hat{d}_{ij})^2}{\sum_{i<j} d_{ij}^2}}$$

Cercano a 0 es ideal. $> 0.2$ indica pobre preservación.

### 4.4 Residual Variance

$$1 - R^2(d_G, d_Y)$$

Cercano a 0 es ideal (buena preservación de estructura geométrica).

### 4.5 Classification Accuracy

KNN ($k_c=5$) y SVM (kernel RBF) sobre $\mathbf{Y}$ con validación cruzada de 5 folds.

### 4.6 Silhouette Score

$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

$s \in [-1, 1]$. Cercano a 1 indica clusters bien separados.

---

## 5. Análisis de Sensibilidad al Parámetro k

### Trade-off Local vs Global

| k bajo | k alto |
|--------|--------|
| ✅ Captura geometría local | ❌ Suaviza geometría local |
| ❌ Riesgo de grafo desconectado | ✅ Grafo siempre conectado |
| ❌ Sensible a ruido | ❌ Cortocircuitos |

### Rango Recomendado

Heurística: $k \in [\log(n), \sqrt{n}]$. Para $n = 1500$: $k \in [7, 39]$.

---

## Referencias

1. Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric framework for nonlinear dimensionality reduction. *Science*, 290(5500), 2319-2323.
2. Roweis, S. T., & Saul, L. K. (2000). Nonlinear dimensionality reduction by locally linear embedding. *Science*, 290(5500), 2323-2326.
3. Venna, J., & Kaski, S. (2006). Local multidimensional scaling. *Neural Networks*, 19(6-7), 889-899.
4. Van der Maaten, L., Postma, E., & Van den Herik, J. (2009). Dimensionality reduction: A comparative review. *JMLR*, 10, 66-71.
5. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *JMLR*, 12, 2825-2830.
