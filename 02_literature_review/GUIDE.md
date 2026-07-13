<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 📚 Guía: Literature Review

## ¿Qué debe contener esta carpeta?

1. `literature_review.md` — Documento principal de revisión bibliográfica
2. `search_log.md` — Registro de búsquedas realizadas (para evitar duplicados)
3. `papers/` — PDFs de los artículos seleccionados (3-5 papers recientes)

## Estrategia de Búsqueda

### Bases de Datos y Repositorios

| Repositorio | URL | Tipo de Búsqueda |
|---|---|---|
| Google Scholar | scholar.google.com | General, citaciones |
| IEEE Xplore | ieeexplore.ieee.org | Conferencias, journals |
| ACM Digital Library | dl.acm.org | Computer science |
| arXiv | arxiv.org | Preprints recientes |
| Springer Link | link.springer.com | Journals, libros |
| ScienceDirect | sciencedirect.com | Journals Elsevier |
| Semantic Scholar | semanticscholar.org | AI-powered search |

### Palabras Clave Sugeridas

Combinar los siguientes términos:

**Grupo 1 (Método):**
- "Isomap"
- "Locally Linear Embedding" OR "LLE"
- "manifold learning"
- "nonlinear dimensionality reduction"

**Grupo 2 (Parámetro):**
- "nearest neighbors" OR "k-nearest"
- "neighborhood size"
- "hyperparameter selection"
- "parameter sensitivity"

**Grupo 3 (Evaluación):**
- "embedding quality"
- "trustworthiness"
- "classification accuracy"
- "dimensionality reduction evaluation"

### Queries de Búsqueda Recomendadas

1. **Google Scholar:**
   ```
   "Isomap" OR "Locally Linear Embedding" "nearest neighbors" "embedding quality" 
   ```
   Filtrar: últimos 5 años (2021-2026)

2. **IEEE Xplore:**
   ```
   (("Isomap" OR "LLE") AND "neighborhood" AND "dimensionality reduction")
   ```

3. **arXiv:**
   ```
   cat:cs.LG AND (isomap OR "locally linear embedding") AND neighbors
   ```

4. **Semantic Scholar:**
   ```
   manifold learning nearest neighbors sensitivity analysis
   ```

5. **ACM Digital Library:**
   ```
   "manifold learning" AND "parameter selection" AND ("Isomap" OR "LLE")
   ```

### Criterios de Selección de Papers

✅ **Incluir:**
- Publicados entre 2019-2026
- Relacionados directamente con Isomap, LLE, o manifold learning
- Que analicen el efecto de hiperparámetros
- Que propongan métricas de evaluación de embeddings
- Que comparen métodos de reducción de dimensionalidad

❌ **Excluir:**
- Papers anteriores a 2018 (salvo los seminales: Tenenbaum 2000, Roweis & Saul 2000)
- Papers que solo usen los métodos sin analizarlos
- Papers en idiomas distintos a inglés o español

## Formato de Registro de Papers

Para cada paper en `literature_review.md`, usar:

```markdown
### [ID] Apellido et al. (Año)
- **Título:** Título completo del paper
- **Autores:** Lista completa
- **Publicación:** Nombre del journal/conferencia
- **DOI/URL:** enlace
- **Resumen:** 3-5 oraciones sobre el contenido
- **Relevancia:** ¿Por qué es relevante para nuestro proyecto?
- **Contribuciones clave:** Lista de aportes principales
- **Métricas utilizadas:** Qué métricas de evaluación usan
- **Datasets:** Qué datasets usan
- **Limitaciones:** Qué limitaciones identifican
- **Citas clave:** Frases textuales útiles con número de página
```

## Cómo Evitar Duplicados

1. Antes de agregar un paper, buscar por DOI en `search_log.md`
2. Verificar que el título no esté ya registrado
3. Usar el formato [ID] consistente (P01, P02, P03...)
4. Actualizar `search_log.md` inmediatamente al encontrar un paper

## Distribución del Trabajo

| Responsable | Búsqueda en | Papers asignados |
|---|---|---|
| Elmer | Google Scholar, Semantic Scholar | P01, P02 |
| Jean Pierre | IEEE Xplore, ACM DL | P03, P04 |
| Christian | arXiv, Springer | P05 |

## Estado
- **Fecha de inicio:** 12 de julio de 2026
- **Fecha límite recolección:** 15 de julio de 2026
- **Fecha límite revisión completa:** 18 de julio de 2026
