# 📋 Registro de búsquedas — Literature Review

**Proyecto:** *Comparación de embeddings basados en variedades y descriptores topológicos para clasificación de imágenes: exactitud, robustez y complejidad computacional*  
**Bases consultadas:** Scopus, Web of Science Core Collection e IEEE Xplore

Este archivo registra las búsquedas realizadas, los filtros aplicados, los archivos exportados y los artículos finalmente seleccionados. Su finalidad es evitar duplicaciones y permitir la reproducción de la estrategia de búsqueda.

## 1. Criterios de búsqueda

### Criterios de inclusión

- Publicaciones entre 2021 y 2026.
- Artículos de revista o trabajos completos de conferencia.
- Publicaciones en inglés.
- Estudios relacionados con clasificación o reconocimiento de imágenes.
- Uso de métodos basados en variedades (*manifold learning*) o descriptores topológicos basados en homología persistente/TDA.
- Inclusión de evidencia sobre al menos uno de los tres ejes: exactitud, robustez o complejidad computacional.

### Criterios de exclusión

- Trabajos exclusivamente teóricos sin aplicación a clasificación de imágenes.
- Estudios de segmentación, detección o recuperación sin resultados de clasificación pertinentes.
- Uso de términos como “manifold” o “topological” con un significado ajeno a los métodos estudiados.
- Resúmenes, editoriales, capítulos no arbitrados, patentes o registros sin información metodológica suficiente.
- Duplicados entre bases de datos.

## 2. Resumen del registro

| Fecha | Repositorio | Búsqueda | Registros exportados | Papers seleccionados |
|---|---|---|---:|---|
| 2026-07-19 | Scopus | Ecuación combinada: variedades o TDA + clasificación de imágenes + evaluación | 222 | P01, P02, P03, P04, P05 |
| 2026-07-19 | WoS Core Collection | Ecuación combinada equivalente en campo `TS` | 107 | P01, P04 |
| 2026-07-19 | IEEE Xplore | Búsqueda amplia de cobertura | 100 exportados | P03, P05 |
| 2026-07-19 | IEEE Xplore | Búsqueda refinada con términos de evaluación | 30 exportados | P04 |
|  |  | **Total antes de deduplicar** |  | **459** | **5 estudios únicos** |

> **Nota:** “Registros exportados” no significa “estudios relevantes”. Los 459 registros fueron sometidos a deduplicación y cribado por título y resumen. Un mismo paper puede aparecer en varias bases; por eso los papers seleccionados de las filas no deben sumarse.

## 3. Ecuaciones utilizadas

### 3.1. Scopus

**Campos consultados:** título, resumen y palabras clave (`TITLE-ABS-KEY`).

```text
TITLE-ABS-KEY(
  (
    "manifold learning"
    OR "manifold-based embedding*"
    OR "nonlinear dimensionality reduction"
    OR ISOMAP
    OR "locally linear embedding"
    OR UMAP
    OR "topological data analysis"
    OR "persistent homology"
    OR "topological descriptor*"
    OR "persistence diagram*"
    OR "persistence image*"
    OR "persistence landscape*"
  )
  AND
  (
    "image classification"
    OR "image recognition"
    OR "visual classification"
  )
  AND
  (
    accurac*
    OR robust*
    OR noise
    OR perturbation*
    OR occlusion
    OR "computational complexity"
    OR runtime
    OR efficiency
    OR scalab*
  )
)
AND PUBYEAR > 2018
AND PUBYEAR < 2027
AND (LIMIT-TO(DOCTYPE, "ar") OR LIMIT-TO(DOCTYPE, "cp"))
AND LIMIT-TO(LANGUAGE, "English")
```

**Resultado:** 222 registros exportados en formato BibTeX.  
**Archivo:** `scopus_export_Jul 19-2026_bfdf8672-57f4-49bc-aa0c-c1fec1e7c0da.bib`.

### 3.2. Web of Science Core Collection

**Campo consultado:** tema (`TS`), que comprende título, resumen, palabras clave del autor y Keywords Plus.

```text
TS=(
  (
    "manifold learning"
    OR "manifold-based embedding*"
    OR "nonlinear dimensionality reduction"
    OR ISOMAP
    OR "locally linear embedding"
    OR UMAP
    OR "topological data analysis"
    OR "persistent homology"
    OR "topological descriptor*"
    OR "persistence diagram*"
    OR "persistence image*"
    OR "persistence landscape*"
  )
  AND
  (
    "image classification"
    OR "image recognition"
    OR "visual classification"
  )
  AND
  (
    accurac*
    OR robust*
    OR noise
    OR perturbation*
    OR occlusion
    OR "computational complexity"
    OR runtime
    OR efficiency
    OR scalab*
  )
)
```

**Filtros aplicados en la interfaz:**

- Años de publicación: 2019–2026.
- Tipos de documento: Article y Proceedings Paper.
- Idioma: English.
- Índice: Web of Science Core Collection.

**Resultado:** 107 registros exportados.  

### 3.3. IEEE Xplore — búsqueda amplia de cobertura

IEEE Xplore requirió una formulación más compacta. La primera consulta priorizó sensibilidad para recuperar trabajos de ambas familias.

```text
(
  ("All Metadata":"manifold learning")
  OR ("All Metadata":"manifold-based embedding")
  OR ("All Metadata":"nonlinear dimensionality reduction")
  OR ("All Metadata":"ISOMAP")
  OR ("All Metadata":"locally linear embedding")
  OR ("All Metadata":"UMAP")
  OR ("All Metadata":"topological data analysis")
  OR ("All Metadata":"persistent homology")
  OR ("All Metadata":"persistence diagram")
  OR ("All Metadata":"persistence image")
)
AND
(
  ("All Metadata":"image classification")
  OR ("All Metadata":"image recognition")
)
```

**Filtros aplicados:** 2019–2026, Journals y Conferences, idioma inglés.  
**Resultado:** 100 registros exportados.  



## 4. Procedimiento de selección

1. Se reunieron los cuatro archivos de exportación: uno de Scopus, uno de WoS y dos de IEEE Xplore.
2. Los registros se normalizaron y deduplicaron primero por DOI y, cuando este no estaba disponible, por título normalizado.
3. Se realizó cribado automático inicial de título, resumen y palabras clave con términos de método, clasificación, exactitud, robustez y complejidad.
4. Los candidatos mejor posicionados fueron examinados manualmente para confirmar que el método geométrico o topológico participara realmente en la clasificación.
5. Se seleccionaron cinco trabajos que cubren ambos grupos metodológicos y contienen evidencia útil para al menos uno de los tres criterios comparativos.
6. Se verificaron DOI, metadatos bibliográficos y disponibilidad del texto completo. En P02 solo estuvo accesible el resumen público; esta restricción quedó declarada en la revisión.

## 5. Papers identificados — Master List

| ID | Título | Autores | Año | DOI | Bases en las que apareció | Estado | Asignado a |
|---|---|---|---:|---|---|---|---|
| P01 | Graph convolutional networks based on manifold learning for semi-supervised image classification | Valem, Pedronette y Latecki | 2023 | [10.1016/j.cviu.2022.103618](https://doi.org/10.1016/j.cviu.2022.103618) | Scopus; WoS | ✅ Revisado y registrado | Elmer |
| P02 | Dimensionality reduction and classification for hyperspectral image based on robust supervised ISOMAP | Ding, Keal, Zhao y Yu | 2022 | [10.1080/21681015.2021.1952657](https://doi.org/10.1080/21681015.2021.1952657) | Scopus | ✅ Revisado; texto completo pendiente | Elmer |
| P03 | PHG-Net: Persistent homology guided medical image classification | Peng, Wang, Sonka y Chen | 2024 | [10.1109/WACV57701.2024.00741](https://doi.org/10.1109/WACV57701.2024.00741) | IEEE Xplore; Scopus | ✅ Revisado y registrado | Jean Pierre |
| P04 | Persistent homology meets object unity: Object recognition in clutter | Samani y Banerjee | 2024 | [10.1109/TRO.2023.3343994](https://doi.org/10.1109/TRO.2023.3343994) | IEEE Xplore; Scopus; WoS | ✅ Revisado y registrado | Jean Pierre |
| P05 | Integrating multi-scale and multi-filtration topological features for medical image classification | Gu et al. | 2026 | [10.1109/WACV61042.2026.00835](https://doi.org/10.1109/WACV61042.2026.00835) | IEEE Xplore; Scopus | ✅ Revisado y registrado | Christian |

## 6. Control de versiones del registro

| Fecha | Cambio realizado |
|---|---|
| 2026-07-19 | Registro inicial de las consultas en Scopus, WoS e IEEE Xplore; incorporación de resultados exportados y lista maestra P01–P05. |

## Estados posibles

- 🔍 Por revisar
- 📖 En lectura
- ✅ Revisado y registrado
- ⚠️ Revisado con acceso parcial
- ❌ Descartado — indicar la razón

