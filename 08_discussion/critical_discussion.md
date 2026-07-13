<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# Discusión Crítica de Resultados

**Responsables:** Elmer Gomez Alcos (líder), Christian Chiroque Ruiz (co-líder)

---

## 1. Resumen de Hallazgos Principales

> TODO: Completar después de ejecutar los experimentos.

- ¿Cómo afecta k a Isomap?
- ¿Cómo afecta k a LLE?
- ¿Cuál método es más robusto a variaciones de k?
- ¿Existe un rango de k que funcione bien para ambos métodos?

## 2. Interpretación de Resultados

### 2.1 Comportamiento de Isomap
> TODO: Analizar por qué Isomap se comporta de cierta manera con k bajo vs alto.

### 2.2 Comportamiento de LLE
> TODO: Analizar la sensibilidad de LLE a k.

### 2.3 Relación entre Conectividad y Calidad
> TODO: Discutir cómo el número de componentes conectadas del grafo afecta los resultados.

## 3. Comparación con la Literatura

> TODO: Contrastar nuestros resultados con los hallazgos de los papers revisados.

- ¿Coinciden nuestros resultados con Tenenbaum et al. (2000)?
- ¿Hay discrepancias con estudios recientes?
- ¿Qué aporta nuestro estudio?

## 4. Limitaciones del Estudio

1. **Número limitado de datasets** — Solo 1 sintético + 1 real
2. **Variable única** — Solo se varía k, no d ni n_samples
3. **Implementaciones estándar** — Uso de sklearn (no implementación propia)
4. **Métricas seleccionadas** — Podrían no capturar todos los aspectos de calidad
5. **Dimensionalidad moderada** — Los datasets usados no son de alta dimensionalidad
6. **Seed fijo** — Resultados podrían variar con diferentes semillas aleatorias

## 5. Trabajo Futuro

- [ ] Explorar otros métodos (t-SNE, UMAP, autoencoder) como comparación
- [ ] Variar la dimensión del embedding (d = 2, 3, 5, 10)
- [ ] Probar con datasets de mayor dimensionalidad (imágenes, texto)
- [ ] Implementar métodos automáticos de selección de k
- [ ] Análisis de estabilidad con múltiples random seeds
- [ ] Incorporar métricas topológicas (persistencia, números de Betti)

## 6. Implicaciones Prácticas

### Guía para seleccionar k
> TODO: Basado en los resultados, proporcionar recomendaciones prácticas.

### Cuándo usar Isomap vs LLE
> TODO: Basado en los resultados, recomendar cuándo usar cada método.
