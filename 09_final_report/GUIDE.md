<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Facultad de Ingeniería de Sistemas e Informática
### Unidad de Posgrado
**Doctorado en DeepTech con enfoque en Inteligencia Artificial y Tecnologías Emergentes**

---

# 📄 Guía para la Elaboración del Informe Final (Final Report)

</div>

Esta carpeta está destinada a la compilación y redacción del artículo o informe científico final del proyecto, el cual debe contar con una extensión de **8 a 15 páginas** y ser entregado el **2 de agosto de 2026**.

## 📂 Estructura Recomendada del Informe (`report.md`)

Para cumplir con el nivel doctoral y las exigencias académicas, se sugiere la siguiente estructura en formato científico (tipo IEEE o Springer):

1. **Título del Proyecto** (Descriptivo e innovador)
2. **Resumen (Abstract)** (Máximo 250 palabras en español e inglés) y **Palabras Clave (Keywords)**
3. **1. Introducción**
   - Contexto de la reducción de dimensionalidad no lineal.
   - Planteamiento del problema (la sensibilidad de Isomap y LLE al hiperparámetro $k$).
   - Objetivos del estudio y contribuciones del equipo.
4. **2. Revisión de la Literatura (State of the Art)**
   - Síntesis de los 3 a 5 papers de investigación reciente analizados.
   - Gaps en el estudio del parámetro de vecindario en variedades geométricas complejas.
5. **3. Fundamentos Matemáticos**
   - Formulación detallada de **Isomap** (grafo de proximidad, Dijkstra, MDS clásico).
   - Formulación detallada de **LLE** (pesos de reconstrucción, matriz de Gram, eigendecomposición de la matriz de costo $\mathbf{M}$).
   - Métricas de preservación local/global (Trustworthiness, Continuity, Stress, Residual Variance).
6. **4. Metodología Experimental**
   - Descripción de los datasets (Sintético: Swiss Roll; Real: MNIST subset/Wine/etc.).
   - Rango del sweep del parámetro $k$ ($k \in [3, 50]$).
   - Clasificadores de evaluación en espacio latente (k-NN, SVM).
7. **5. Resultados e Ilustraciones**
   - Tablas comparativas de desempeño para cada $k$.
   - Gráficos de evolución de métricas vs $k$.
   - Proyecciones visuales de los embeddings generados.
8. **6. Discusión Crítica**
   - Interpretación del comportamiento de cada algoritmo frente al sub-ajuste o sobre-ajuste vecinal (cortocircuitos topológicos).
   - Limitaciones del estudio y comparativas de robustez.
9. **7. Conclusiones y Trabajo Futuro**
   - Respuestas a la pregunta de investigación e implicaciones prácticas.
10. **8. Referencias** (Formato APA 7 u orden alfabético de citación científica).

---

## 🛠️ Directrices de Colaboración para la Escritura

Para evitar conflictos de edición y mantener una redacción homogénea:

- **Redacción en Markdown/LaTeX:** Todo el contenido matemático debe usar la notación de LaTeX estándar en el archivo `report.md`.
- **Integración de Imágenes:** Las figuras finales generadas en `07_visualizations/figures` deben ser copiadas a `09_final_report/assets/` y enlazadas en el reporte usando la ruta relativa `assets/nombre_imagen.png`.
- **Distribución de Secciones:**
  - *Elmer Gomez:* Introducción, Resultados de Isomap, Discusión.
  - *Jean Pierre Tincopa:* Metodología, Visualizaciones, Resultados de Comparación, Compilación del reporte.
  - *Christian Chiroque:* Fundamento Matemático, Resultados de LLE, Conclusiones y Referencias.
