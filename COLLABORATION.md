<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

</div>

---

# 🤝 Guía de Colaboración

## 👥 Asignación de Roles

### Elmer Valerio Gomez Alcos — Líder de Investigación y Experimentos
- 📚 Literature review (co-líder)
- 🧪 Experimentos con Isomap (variando k)
- 💬 Critical discussion (co-líder)
- 📄 Informe: Introducción, Resultados Isomap, Discusión
- 🎤 Presentación: Introducción, Motivación, Problema, Discusión

### Jean Pierre Tincopa Flores — Líder de Implementación y Visualización
- 💻 Implementation lead (data loading, metrics, code architecture)
- 📊 Pipeline de visualización
- 📚 Literature review (co-líder)
- 📄 Informe: Metodología, Visualizaciones, Resultados Comparación
- 🎤 Presentación: Métricas, Diseño Experimental, Conclusiones

### Christian Chiroque Ruiz — Líder de Fundamento Teórico y LLE
- 🔢 Mathematical background (líder)
- 🧪 Experimentos con LLE (variando k)
- 💬 Critical discussion (co-líder)
- 📄 Informe: Fundamento Matemático, Resultados LLE, Conclusiones
- 🎤 Presentación: Fundamento Isomap, Fundamento LLE, Limitaciones

---

## 🔀 Flujo de Trabajo con Git

### Ramas
- `main` — Rama principal (protegida)
- `feature/<nombre>-<descripcion>` — Ramas de trabajo

### Ejemplos:
```
feature/elmer-isomap-experiments
feature/jeanpierre-data-loader
feature/christian-math-background
```

### Formato de Commits
```
[AREA] Descripción corta
```

| Código | Área |
|--------|------|
| `[LIT]` | Literature Review |
| `[MATH]` | Mathematical Background |
| `[IMPL]` | Implementation |
| `[EXP]` | Experiments |
| `[VIZ]` | Visualizations |
| `[EVAL]` | Evaluation |
| `[DISC]` | Discussion |
| `[REPORT]` | Final Report |
| `[PRES]` | Presentation |
| `[DOCS]` | Documentation |

### Pull Requests
- Requerido para merge a `main`
- Al menos 1 review de otro integrante

---

## 📱 Comunicación

| Canal | Uso |
|-------|-----|
| WhatsApp/Telegram | Comunicación diaria |
| Google Meet | Standup diario (15 min) |
| GitHub Issues | Tracking de tareas |
| GitHub PRs | Code review |

---

## 📝 Convenciones de Código

- **Python:** 3.10+
- **Estilo:** PEP 8
- **Docstrings:** Google style
- **Type hints:** Obligatorios
- **Random seed:** 42
- **Notebooks:** Celdas markdown explicativas en español
