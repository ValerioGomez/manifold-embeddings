<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 📊 Guía: Performance Comparison

## ¿Qué debe contener esta carpeta?

El archivo `performance_comparison.md` con el análisis comparativo de rendimiento.

## Estructura del Análisis

### 1. Tabla Resumen de Métricas
Para cada combinación (método, dataset, k), mostrar todas las métricas.

### 2. Análisis por Métrica
Para cada métrica:
- ¿Cómo varía con k?
- ¿Cuál método es más estable?
- ¿Cuál es el k óptimo para cada método?

### 3. Ranking de Métodos
- Por cada métrica, rankear Isomap vs LLE
- Identificar fortalezas y debilidades de cada método

### 4. Análisis Estadístico (opcional)
- Test de significancia si se repiten experimentos con distintos seeds
- Intervalos de confianza

### 5. Recomendaciones
- ¿Qué método usar según el tipo de datos?
- ¿Qué rango de k es generalmente seguro?

## Tablas Esperadas

### Tabla 1: Métricas por k (Isomap - Swiss Roll)
| k | Trust. | Cont. | Stress | Res. Var. | Acc KNN | Acc SVM | Silhouette | Time (s) |

### Tabla 2: Métricas por k (LLE - Swiss Roll)
(misma estructura)

### Tabla 3: Métricas por k (Isomap - [Real Dataset])
### Tabla 4: Métricas por k (LLE - [Real Dataset])

### Tabla 5: Mejor k por método y métrica
| Métrica | Mejor k (Isomap) | Valor | Mejor k (LLE) | Valor |

## Estado
- **Responsables:** TODOS
- **Fecha límite:** 22 de julio de 2026
