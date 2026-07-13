---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f7
color: #1d1d1f
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }
  h1 {
    color: #003366;
  }
  h2 {
    color: #003366;
  }
  footer {
    font-size: 0.5em;
    color: #86868b;
  }
---

# Impacto de Vecinos Cercanos ($k$) en Embeddings de Isomap y LLE
### Estudio Comparativo en Clasificación y Calidad Geométrica

**Universidad Nacional Mayor de San Marcos**  
*Doctorado en DeepTech — Inteligencia Artificial y Tecnologías Emergentes*

**Autores:** Elmer Gomez | Jean Pierre Tincopa | Christian Chiroque  
**Fecha:** Agosto 2026

---

## Agenda de la Presentación

1. **Introducción & Hipótesis del Manifold**
2. **Fundamentos Matemáticos** (Isomap & LLE)
3. **Métricas de Preservación y Calidad**
4. **Diseño Experimental & Sweeps de $k$**
5. **Resultados** (Sintéticos & Reales)
6. **Discusión Crítica & Limitaciones**
7. **Conclusiones**

---

## 1. Introducción y Motivación

- **El Desafío de la Alta Dimensionalidad:** Maldición de la dimensionalidad en DeepTech.
- **Hipótesis del Manifold:** Los datos de alta dimensión suelen residir cerca de una variedad subyacente $\mathcal{M}$ de dimensión mucho menor ($d \ll D$).
- **La Sensibilidad al Vecindario ($k$):**
  - ¿Cómo afecta la conectividad local la reconstrucción global?
  - Impacto en fidelidad geométrica y precisión de clasificadores.

---

## 2. Fundamentos de Isomap (Isometric Mapping)

- **Preservación de Distancias Geodésicas:** Mapeo isométrico global.
- **Flujo de Ejecución:**
  1. Construcción del grafo de vecindarios $k$-NN.
  2. Cálculo del camino más corto (Dijkstra / Floyd-Warshall) para aproximar la distancia geodésica $\mathbf{D}_G$.
  3. Aplicación de MDS clásico: Double centering sobre $\mathbf{D}_G^2$ para encontrar la matriz de producto interno $\mathbf{B}$ y sus componentes principales.

---

## 3. Fundamentos de LLE (Locally Linear Embedding)

- **Preservación de Relaciones Lineales Locales:** Parches localmente planos.
- **Flujo de Ejecución:**
  1. Encontrar $k$ vecinos cercanos para cada punto.
  2. Calcular pesos de reconstrucción lineal $\mathbf{W}$ que minimizan el error cuadrático local.
  3. Encontrar coordenadas de baja dimensión $\mathbf{Y}$ minimizando la reconstrucción global mediante eigendecomposición de $\mathbf{M} = (\mathbf{I} - \mathbf{W})^T(\mathbf{I} - \mathbf{W})$.

---

## 4. Métricas de Evaluación de Embeddings

- **Métricas Geométricas:**
  - **Trustworthiness ($T$):** Verifica si el espacio de salida no introduce falsos vecinos.
  - **Continuity ($C$):** Verifica si el espacio de salida preserva los vecinos originales.
  - **Kruskal Stress:** Pérdida de distancias relativas.
- **Evaluación Downstream:**
  - Accuracy de clasificación mediante **k-NN** y **SVM** con validación cruzada.
  - Silhoutte score para evaluar separación de clases.

---

## 5. Diseño Experimental

- **Dataset Sintético:** *Swiss Roll* (curvatura continua ideal).
- **Dataset Real:** *Wine Dataset / subset MNIST*.
- **Sweep de Parámetro:**
  - $k \in \{3, 5, 7, 10, 15, 20, 25, 30, 40, 50\}$.
- **Clasificación:** Validación cruzada de 5 folds sobre el espacio bidimensional proyectado.

---

## 6. Resultados: Métricas de Calidad vs $k$

*Aquí se insertarán los gráficos generados en el pipeline de visualización:*
- Evolución de la **Trustworthiness** y **Continuity** con la variación de $k$.
- Evolución del **Stress** y tiempo de ejecución.
- Evolución de la **Exactitud (Accuracy)** en clasificación KNN y SVM.

---

## 7. Discusión Crítica: Isomap vs LLE

- **Isomap:**
  - Sensible a "cortocircuitos" topológicos cuando $k$ es demasiado grande.
  - Robusto globalmente cuando el grafo está totalmente conectado.
- **LLE:**
  - Alta inestabilidad matemática cuando $k$ es muy pequeño (matriz singular).
  - Pérdida de localidad cuando $k$ excede el límite del espacio localmente plano.

---

## 8. Conclusiones

- **Compromiso Topológico:** No existe un $k$ universal; el rango óptimo se encuentra entre $[\log(n), \sqrt{n}]$.
- **Recomendaciones Prácticas:**
  - Usar Isomap cuando se requiere conservar la estructura global del manifold.
  - Usar LLE para manifolds muy enroscados con vecindarios locales bien delimitados y menor coste computacional.

---

## Preguntas y Comentarios

### Muchas Gracias por su Atención
*Unidad de Posgrado - FISI - UNMSM*

**Contactos del Equipo:**
- elmer.gomeza@unmsm.edu.pe
- jean.tincopaf@unmsm.edu.pe
- christian.chiroquer@unmsm.edu.pe
