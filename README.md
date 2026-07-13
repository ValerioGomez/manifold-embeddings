<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Facultad de Ingeniería de Sistemas e Informática
### Unidad de Posgrado
**Doctorado en DeepTech con enfoque en Inteligencia Artificial y Tecnologías Emergentes**

---

# Manifold Embeddings: Impacto del Número de Vecinos Cercanos en Isomap y LLE

**Curso:** [Nombre del curso — por definir]

</div>

---

## 📋 Información del Proyecto

### Integrantes

| # | Nombre Completo | Correo Institucional |
|---|----------------|----------------------|
| 1 | Elmer Valerio Gomez Alcos | elmer.gomeza@unmsm.edu.pe |
| 2 | Jean Pierre Tincopa Flores | jean.tincopaf@unmsm.edu.pe |
| 3 | Christian Chiroque Ruiz | christian.chiroquer@unmsm.edu.pe |

### Planteamiento del Problema

Los métodos de reducción de dimensionalidad basados en manifolds — en particular **Isomap** (Isometric Feature Mapping) y **LLE** (Locally Linear Embedding) — son técnicas fundamentales en el aprendizaje automático y la visualización de datos de alta dimensionalidad. Ambos algoritmos dependen críticamente de un hiperparámetro clave: el **número de vecinos cercanos (k)**.

Sin embargo, la selección de *k* suele realizarse de forma heurística o por defecto, sin una comprensión sistemática de cómo este parámetro afecta:

- La **calidad del embedding** resultante (preservación de la estructura geométrica local y global).
- El **rendimiento en tareas downstream**, como la clasificación supervisada sobre el espacio reducido.
- La **estabilidad y robustez** de las representaciones ante variaciones de *k*.

Este proyecto aborda la pregunta: **¿Cómo impacta la variación del número de vecinos cercanos (k) en los embeddings producidos por Isomap y LLE, y cuál es su efecto cuantificable en la precisión de clasificación y la calidad del embedding?**

### Fechas Clave

| Entregable | Fecha Límite |
|-----------|--------------|
| Todos los componentes del proyecto (propuesta, revisión bibliográfica, fundamento matemático, implementación, experimentos, evaluación, visualizaciones, discusión crítica) | **26 de julio de 2026** |
| Informe final y presentación | **2 de agosto de 2026** |

---

## 🎯 Objetivo del Proyecto

### Objetivo General

Investigar de manera sistemática cómo la variación del número de vecinos cercanos (*k*) afecta los embeddings producidos por los algoritmos **Isomap** y **LLE**, cuantificando el impacto en la **precisión de clasificación** y la **calidad del embedding** mediante métricas estandarizadas.

### Objetivos Específicos

1. **Implementar un pipeline experimental** reproducible para generar embeddings con Isomap y LLE bajo distintos valores de *k*.
2. **Evaluar la calidad del embedding** utilizando métricas como *trustworthiness*, *continuity*, *stress* residual y preservación de vecindarios.
3. **Medir el impacto en clasificación** entrenando clasificadores (KNN, SVM) sobre los espacios reducidos y comparando la accuracy para cada valor de *k*.
4. **Comparar ambos métodos** (Isomap vs. LLE) en términos de sensibilidad al parámetro *k* y robustez de las representaciones.
5. **Visualizar y analizar** los resultados para identificar rangos óptimos de *k* y patrones de comportamiento comunes o divergentes entre ambos algoritmos.

---

## 📂 Estructura del Proyecto

```
manifold-embeddings/
├── README.md                          # Este archivo
├── ROADMAP.md                         # Plan de ejecución y cronograma
├── COLLABORATION.md                   # Guía de colaboración del equipo
├── .gitignore                         # Archivos excluidos del control de versiones
├── requirements.txt                   # Dependencias de Python
├── 01_proposal/
│   ├── GUIDE.md                       # Instrucciones para la propuesta
│   └── project_proposal.md            # Propuesta del proyecto (1 página)
├── 02_literature_review/
│   ├── GUIDE.md                       # Instrucciones para la revisión bibliográfica
│   ├── papers/
│   │   └── .gitkeep                   # Directorio para PDFs de papers
│   ├── search_log.md                  # Registro de búsqueda bibliográfica
│   └── literature_review.md           # Revisión de literatura (3-5 papers)
├── 03_mathematical_background/
│   ├── GUIDE.md                       # Instrucciones para el fundamento matemático
│   └── mathematical_background.md     # Formalización matemática de Isomap y LLE
├── 04_implementation/
│   ├── GUIDE.md                       # Instrucciones para la implementación
│   ├── notebooks/
│   │   ├── 01_data_loading.ipynb      # Carga y exploración de datasets
│   │   ├── 02_isomap_experiments.ipynb # Experimentos con Isomap
│   │   ├── 03_lle_experiments.ipynb   # Experimentos con LLE
│   │   ├── 04_comparison_analysis.ipynb # Análisis comparativo
│   │   └── 05_visualizations.ipynb    # Generación de visualizaciones
│   ├── src/
│   │   ├── __init__.py                # Inicialización del paquete
│   │   ├── data_loader.py             # Funciones de carga de datos
│   │   ├── embeddings.py              # Wrappers para Isomap y LLE
│   │   ├── metrics.py                 # Métricas de calidad del embedding
│   │   ├── visualization.py           # Funciones de visualización
│   │   └── utils.py                   # Utilidades generales
│   └── tests/
│       └── test_metrics.py            # Tests unitarios para métricas
├── 05_experiments/
│   ├── GUIDE.md                       # Instrucciones para los experimentos
│   ├── configs/
│   │   └── experiment_config.yaml     # Configuración de experimentos
│   └── results/
│       └── .gitkeep                   # Directorio para resultados
├── 06_evaluation/
│   ├── GUIDE.md                       # Instrucciones para la evaluación
│   └── performance_comparison.md      # Comparación de rendimiento
├── 07_visualizations/
│   ├── GUIDE.md                       # Instrucciones para visualizaciones
│   └── figures/
│       └── .gitkeep                   # Directorio para figuras generadas
├── 08_discussion/
│   ├── GUIDE.md                       # Instrucciones para la discusión
│   └── critical_discussion.md         # Discusión crítica de resultados
├── 09_final_report/
│   ├── GUIDE.md                       # Instrucciones para el informe final
│   ├── report.md                      # Informe final (8-15 páginas)
│   └── assets/
│       └── .gitkeep                   # Directorio para assets del informe
├── 10_presentation/
│   ├── GUIDE.md                       # Instrucciones para la presentación
│   └── slides.md                      # Slides de la presentación (10-12 min)
└── data/
    ├── raw/
    │   └── .gitkeep                   # Datos crudos (no versionados)
    └── processed/
        └── .gitkeep                   # Datos procesados
```

---

## 📦 Entregables

### Componentes del Proyecto — Fecha límite: 26 de julio de 2026

- [ ] **Project Proposal** (1 página) — Propuesta concisa del proyecto con objetivos, metodología y alcance.
- [ ] **Literature Review** (3-5 papers) — Revisión bibliográfica de artículos clave sobre Isomap, LLE y selección de *k*.
- [ ] **Mathematical Background** — Formalización matemática de ambos algoritmos y las métricas de evaluación.
- [ ] **Implementation** (Python/Jupyter) — Código funcional con pipeline de datos, embeddings, métricas y visualización.
- [ ] **Experiments** — Ejecución sistemática de experimentos variando *k* en múltiples datasets.
- [ ] **Performance Comparison** — Tabla comparativa de métricas de calidad y accuracy de clasificación.
- [ ] **Visualizations** — Gráficos de embeddings 2D/3D, curvas de accuracy vs. *k*, heatmaps de métricas.
- [ ] **Critical Discussion** — Análisis crítico de resultados, limitaciones y trabajo futuro.

### Informe y Presentación — Fecha límite: 2 de agosto de 2026

- [ ] **Final Report** (8-15 páginas) — Documento integrador con todas las secciones del proyecto.
- [ ] **Presentation** (10-12 minutos) — Presentación oral con slides de los hallazgos principales.

---

## 🚀 Quick Start

### 1. Clonar el repositorio

```bash
git clone https://github.com/<usuario>/manifold-embeddings.git
cd manifold-embeddings
```

### 2. Crear un entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar los notebooks

```bash
jupyter lab
```

Navegar a `04_implementation/notebooks/` y ejecutar los notebooks en orden:

1. `01_data_loading.ipynb` — Carga y exploración de datos
2. `02_isomap_experiments.ipynb` — Experimentos con Isomap
3. `03_lle_experiments.ipynb` — Experimentos con LLE
4. `04_comparison_analysis.ipynb` — Análisis comparativo
5. `05_visualizations.ipynb` — Generación de visualizaciones finales

### 5. Ejecutar tests

```bash
python -m pytest 04_implementation/tests/ -v
```

---

## 🛠️ Tecnologías Principales

| Tecnología | Uso |
|-----------|-----|
| Python 3.10+ | Lenguaje de programación principal |
| scikit-learn | Implementaciones de Isomap, LLE, clasificadores y métricas |
| NumPy / SciPy | Operaciones numéricas y álgebra lineal |
| Matplotlib / Seaborn | Visualización de datos y resultados |
| Pandas | Manipulación y análisis de datos tabulares |
| JupyterLab | Entorno interactivo para notebooks |
| UMAP / openTSNE | Métodos adicionales de referencia para comparación |

---

## 📜 Licencia

Este proyecto es de **uso académico exclusivo**, desarrollado como parte del programa de Doctorado en DeepTech de la Universidad Nacional Mayor de San Marcos (UNMSM).

Todos los derechos reservados © 2026 — Gomez Alcos, Tincopa Flores, Chiroque Ruiz.

El código y la documentación de este repositorio pueden ser utilizados con fines educativos y de investigación, citando adecuadamente a los autores y a la institución.
