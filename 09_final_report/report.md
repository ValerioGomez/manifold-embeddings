<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Facultad de Ingeniería de Sistemas e Informática
### Unidad de Posgrado
**Doctorado en DeepTech con enfoque en Inteligencia Artificial y Tecnologías Emergentes**

---

# Impacto del Número de Vecinos Cercanos ($k$) en la Calidad de Embeddings Producidos por Isomap y LLE: Un Estudio Comparativo

**Curso:** Aprendizaje de Máquinas Avanzado / Aprendizaje Geométrico  
**Semestre Académico:** 2026-I  
**Fecha de Entrega:** 2 de agosto de 2026  

---

**Integrantes:**
- Elmer Valerio Gomez Alcos (elmer.gomeza@unmsm.edu.pe)
- Jean Pierre Tincopa Flores (jean.tincopaf@unmsm.edu.pe)
- Christian Chiroque Ruiz (christian.chiroquer@unmsm.edu.pe)

---

### Resumen
*El presente artículo presenta un análisis exhaustivo y sistemático de la influencia del número de vecinos cercanos ($k$) sobre la calidad de los embeddings dimensionales producidos por Isomap y Locally Linear Embedding (LLE). Evaluamos el comportamiento de ambos algoritmos bajo escenarios sintéticos (Swiss Roll) y reales (Wine/MNIST Subset) variando $k$ de 3 a 50. Cuantificamos la calidad del embedding a través de métricas de preservación local y global (Trustworthiness, Continuity, Stress y Residual Variance) y el impacto subsiguiente en la precisión de algoritmos de clasificación descendente (k-NN y SVM). Los resultados demuestran que Isomap presenta mayor resiliencia global a costa de mayor carga computacional, mientras que LLE muestra una alta sensibilidad local en la configuración de sus pesos de reconstrucción.*

**Palabras clave:** Manifold Learning, Isomap, LLE, Vecindario Local, Reducción de Dimensionalidad, Preservación Topológica.

</div>

---

## 1. Introducción
*(Sección a redactar por Elmer Valerio Gomez Alcos)*
- **Contexto y Motivación:** Introducción general a la hipótesis del manifold en aprendizaje profundo y DeepTech.
- **Planteamiento del Problema:** Explicación detallada de cómo la correcta elección de $k$ determina si el algoritmo preserva la topología subyacente o introduce distorsiones geométricas.
- **Contribuciones del Trabajo:**
  1. Evaluación sistemática del sweep de $k \in [3, 50]$.
  2. Implementación de una suite de evaluación multivariable.
  3. Análisis estadístico comparativo de robustez y costo computacional.

---

## 2. Revisión de la Literatura
*(Sección coordinada por Elmer Gomez y Jean Pierre Tincopa)*
- **Estado del Arte:** Resumen de las investigaciones científicas sobre métodos de reducción de dimensionalidad no lineal.
- **Discusión de Papers Recientes:**
  - *Paper 1 (ejemplo):* Roweis & Saul (2000) y Tenenbaum et al. (2000) (artículos seminales).
  - *Paper 2-5:* Investigaciones sobre optimización adaptativa del parámetro de vecindario ($k$-adaptativo).

---

## 3. Fundamentos Matemáticos
*(Sección a redactar por Christian Chiroque Ruiz)*

### 3.1 Isometric Feature Mapping (Isomap)
Construcción del grafo de adyacencia ponderado, cálculo del camino más corto (distancias geodésicas $\mathbf{D}_G$) mediante Dijkstra y posterior aplicación de Multidimensional Scaling (MDS) clásico mediante double-centering:
$$\mathbf{B} = -\frac{1}{2} \mathbf{H} \mathbf{D}_G^{(2)} \mathbf{H}$$

### 3.2 Locally Linear Embedding (LLE)
Cálculo de los pesos de reconstrucción locales $\mathbf{W}$ que minimizan:
$$\mathcal{E}(\mathbf{W}) = \sum_{i=1}^{n} \left\| x_i - \sum_{j \in \mathcal{N}_i} w_{ij} x_j \right\|^2$$
y posterior cálculo de la proyección de baja dimensión $\mathbf{Y}$ minimizando la forma cuadrática asociada a la matriz de costo $\mathbf{M} = (\mathbf{I} - \mathbf{W})^T(\mathbf{I} - \mathbf{W})$:
$$\Phi(\mathbf{Y}) = \text{tr}(\mathbf{Y}^T \mathbf{M} \mathbf{Y})$$

### 3.3 Métricas de Calidad de Embeddings
Formulación formal de:
- **Trustworthiness ($T$):** Preservación de vecindades del espacio de salida al original.
- **Continuity ($C$):** Conservación de vecindades del espacio original al de salida.
- **Kruskal Stress:** Medición del error en la preservación de distancias euclidianas.
- **Silhouette Coefficient:** Evaluación de cohesión y separación de agrupaciones.

---

## 4. Metodología Experimental
*(Sección a redactar por Jean Pierre Tincopa Flores)*
- **Estrategia de Selección de Datasets:** Justificación del Swiss Roll (curvatura continua no lineal) y dataset real.
- **Configuración del Experimento:** Descripción del pipeline implementado en Python utilizando `scikit-learn`.
- **Rango del Hiperparámetro:** $k \in \{3, 5, 7, 10, 15, 20, 25, 30, 40, 50\}$.

---

## 5. Resultados
*(Sección colaborativa - Análisis de Datos y Gráficos)*

### 5.1 Caso de Estudio 1: Manifold Sintético (Swiss Roll)
- Tabla comparativa de métricas de calidad y precisión de clasificación.
- Embeddings representativos para $k \in \{5, 15, 40\}$.

### 5.2 Caso de Estudio 2: Datos Reales
- Análisis de la estructura de clasificación SVM y k-NN bajo variaciones del espacio latente inducido por $k$.

---

## 6. Discusión Crítica
*(Sección coordinada por Elmer Gomez y Christian Chiroque)*
- **Comportamiento del Grafo frente a $k$ subdimensionados:** Fragmentación topológica de Isomap y degeneración matemática en LLE.
- **Comportamiento ante $k$ sobredimensionados:** Cortocircuitos de distancias geodésicas en Isomap y pérdida de localidad en la aproximación lineal en LLE.
- **Robustez y Recomendaciones Prácticas:** Cuándo preferir cada método en función del tamaño muestral y la dimensionalidad original.

---

## 7. Conclusiones y Trabajo Futuro
*(Redactado colaborativamente)*
- Síntesis de los hallazgos principales.
- Limitaciones del experimento actual.
- Propuesta de extensión del estudio incorporando métodos probabilísticos (t-SNE) y topológicos (TDA - Persistence Diagrams).

---

## 8. Referencias
*(Formato APA 7 - Mínimo 10 entradas de revistas/conferencias de alto impacto)*
1. Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric framework for nonlinear dimensionality reduction. *Science*, 290(5500), 2319-2323.
2. Roweis, S. T., & Saul, L. K. (2000). Nonlinear dimensionality reduction by locally linear embedding. *Science*, 290(5500), 2323-2326.
3. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
