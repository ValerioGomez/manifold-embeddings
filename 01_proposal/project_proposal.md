<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

---

## Propuesta de Proyecto de Investigación

</div>

---

### Título

**Impacto del Número de Vecinos Cercanos (k) en la Calidad de Embeddings Producidos por Isomap y LLE: Un Estudio Comparativo**

### Integrantes

| Integrante | Correo |
|---|---|
| Elmer Gomez Alcos | elmer.gomez@unmsm.edu.pe |
| Jean Pierre Tincopa | jean.tincopa@unmsm.edu.pe |
| Christian Chiroque | christian.chiroque@unmsm.edu.pe |

### Planteamiento del Problema

Los métodos de *manifold learning*, como Isomap (Tenenbaum et al., 2000) y Locally Linear Embedding — LLE (Roweis & Saul, 2000), constituyen herramientas fundamentales para la reducción no lineal de dimensionalidad. Ambos algoritmos dependen críticamente del hiperparámetro *k* (número de vecinos cercanos), el cual determina la estructura del grafo de vecindad utilizado para aproximar la geometría del *manifold* subyacente. Un valor de *k* demasiado pequeño genera grafos desconectados o embeddings ruidosos, mientras que un *k* excesivamente grande distorsiona la estructura local al incluir puntos que no pertenecen a la misma región del *manifold*, provocando fenómenos de *short-circuiting*.

A pesar del uso generalizado de estos métodos en aplicaciones de visión por computadora, bioinformática y análisis exploratorio de datos, existe un vacío en la literatura respecto al análisis sistemático de cómo la elección de *k* afecta simultáneamente la calidad intrínseca del embedding (trustworthiness, continuity, stress residual) y el desempeño en tareas downstream como clasificación. La mayoría de los estudios existentes seleccionan *k* de manera heurística o reportan resultados para un solo valor, sin explorar la sensibilidad del método a este parámetro.

Este proyecto busca llenar dicho vacío mediante un estudio comparativo riguroso que evalúe el impacto de *k* en un rango amplio (3 ≤ k ≤ 50), utilizando tanto datos sintéticos con estructura de *manifold* conocida como datasets reales de referencia, y empleando métricas tanto intrínsecas como extrínsecas.

### Objetivos

**Objetivo General:** Investigar y cuantificar la sensibilidad de Isomap y LLE al número de vecinos cercanos *k*, evaluando su impacto en la calidad de los embeddings producidos y en el desempeño de tareas de clasificación posteriores.

**Objetivos Específicos:**

1. Implementar los algoritmos Isomap y LLE con valores de *k* variando sistemáticamente en el rango [3, 50].
2. Medir la calidad intrínseca de los embeddings generados mediante las métricas de *trustworthiness*, *continuity*, varianza residual y error de reconstrucción.
3. Evaluar la precisión de clasificación sobre los datos embebidos utilizando clasificadores KNN y SVM.
4. Comparar la robustez de Isomap frente a LLE ante cambios en el valor de *k*, identificando rangos óptimos para cada método.

### Metodología

- **Datasets:** Swiss Roll (sintético, 1500 puntos, 3D → 2D) y un dataset real seleccionado entre MNIST digits (subconjunto), Wine o Breast Cancer de scikit-learn.
- **Variación de *k*:** Se explorará *k* ∈ {3, 5, 7, 10, 15, 20, 30, 40, 50}.
- **Métricas intrínsecas:** Trustworthiness, continuity (Venna & Kaski, 2006), varianza residual (Isomap), error de reconstrucción (LLE).
- **Métricas extrínsecas:** Accuracy de clasificación con KNN (k_clf = 5) y SVM (kernel RBF) mediante validación cruzada 5-fold.
- **Herramientas:** Python 3.11+, scikit-learn, matplotlib, NumPy.
- **Visualización:** Scatter plots 2D coloreados por clase/etiqueta, curvas de métricas vs. *k*.

### Resultados Esperados

1. Curvas de sensibilidad que muestren cómo cada métrica de calidad varía en función de *k* para ambos métodos.
2. Identificación de rangos de *k* óptimos (y subóptimos) para Isomap y LLE en cada dataset.
3. Evidencia cuantitativa sobre cuál de los dos métodos es más robusto a la elección de *k*.
4. Recomendaciones prácticas para la selección de *k* basadas en los resultados experimentales.

### Referencias

1. Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric framework for nonlinear dimensionality reduction. *Science*, *290*(5500), 2319–2323. https://doi.org/10.1126/science.290.5500.2319
2. Roweis, S. T., & Saul, L. K. (2000). Nonlinear dimensionality reduction by locally linear embedding. *Science*, *290*(5500), 2323–2326. https://doi.org/10.1126/science.290.5500.2323
3. Venna, J., & Kaski, S. (2006). Local multidimensional scaling. *Neural Networks*, *19*(6-7), 889–899. https://doi.org/10.1016/j.neunet.2006.05.014
4. Van der Maaten, L., Postma, E., & van den Herik, J. (2009). Dimensionality reduction: A comparative review. *Journal of Machine Learning Research*, *10*, 66–71.
5. Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, *12*, 2825–2830.

---

<div align="center">

*Fecha de elaboración: 12 de julio de 2026*

</div>
