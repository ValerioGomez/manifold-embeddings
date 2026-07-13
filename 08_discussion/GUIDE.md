<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 💬 Guía: Critical Discussion

## ¿Qué debe contener esta carpeta?

El archivo `critical_discussion.md` con el análisis crítico de los resultados.

## Estructura de la Discusión

### 1. Resumen de Hallazgos Principales
- ¿Cómo afecta k a cada método?
- ¿Cuál método es más robusto?
- ¿Hay un k "universal" que funcione bien?

### 2. Interpretación de Resultados
- ¿Por qué Isomap se comporta de cierta manera con k bajo/alto?
- ¿Por qué LLE tiene problemas con ciertos valores de k?
- Relación entre conectividad del grafo y calidad del embedding

### 3. Comparación con la Literatura
- ¿Nuestros resultados coinciden con lo reportado en la literatura?
- ¿Hay discrepancias? ¿Por qué?

### 4. Limitaciones del Estudio
- Número limitado de datasets
- Solo se varía k (no d, no n_samples)
- Uso de implementaciones de sklearn (no custom)
- Métricas seleccionadas podrían no capturar todo
- Datasets de dimensionalidad moderada

### 5. Trabajo Futuro
- Explorar otros métodos (t-SNE, UMAP)
- Variar dimensión del embedding
- Datasets de mayor dimensionalidad
- Métodos automáticos de selección de k
- Análisis de estabilidad con múltiples seeds

### 6. Implicaciones Prácticas
- Guía práctica para seleccionar k
- Cuándo usar Isomap vs LLE

## Estado
- **Responsables:** Elmer Gomez (lead), Christian Chiroque (co-lead)
- **Fecha límite:** 23 de julio de 2026
