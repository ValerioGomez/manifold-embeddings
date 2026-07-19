<div align="center">

# UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS
### Unidad de Posgrado — Doctorado en DeepTech

---

# Revisión bibliográfica

## Comparación de embeddings basados en variedades y descriptores topológicos para clasificación de imágenes: exactitud, robustez y complejidad computacional

## 1. Introducción

La clasificación de imágenes suele partir de representaciones de muy alta dimensión, ya sea el vector de píxeles o las características obtenidas mediante una red neuronal. En este contexto, los métodos basados en variedades (*manifold learning*) y los descriptores provenientes del análisis topológico de datos (TDA) ofrecen dos maneras diferentes de explotar la estructura geométrica de los datos. Los primeros suponen que las observaciones se concentran cerca de una variedad de dimensión intrínseca menor y buscan preservar relaciones locales o distancias geodésicas. Los segundos resumen propiedades cualitativas —como componentes conexas, ciclos y cavidades— mediante homología persistente, diagramas de persistencia y representaciones vectoriales derivadas.

La presente revisión analiza cinco investigaciones recientes que aplican estos enfoques a clasificación de imágenes. El objetivo no es determinar qué familia es universalmente superior, sino identificar bajo qué condiciones cada representación mejora la exactitud, qué tipo de robustez ha sido realmente evaluado y qué costos computacionales introduce. La pregunta orientadora es: **¿cómo se comparan los embeddings basados en variedades y los descriptores topológicos para clasificación de imágenes en términos de exactitud, robustez y complejidad computacional?**

La búsqueda se limitó a Scopus, Web of Science Core Collection e IEEE Xplore, con publicaciones entre 2019 y 2026 en inglés y relacionadas directamente con clasificación o reconocimiento de imágenes. Los archivos exportados reunieron 459 registros antes de la deduplicación. Después del cribado por título, resumen, pertinencia metodológica y disponibilidad de resultados comparables, se seleccionaron cinco trabajos revisados por pares. La selección busca cubrir ambos enfoques y distintos escenarios: clasificación semisupervisada, imágenes hiperespectrales, imágenes médicas y reconocimiento robótico bajo oclusión. Debe advertirse que el texto completo de Ding et al. (2022) no se encontró en acceso abierto; por ello, su análisis se restringe a la información verificable del resumen y de los metadatos bibliográficos, sin inventar datasets ni resultados numéricos.

## 2. Papers revisados

### P01. Graph convolutional networks based on manifold learning for semi-supervised image classification

**Autores:** Lucas P. Valem, Daniel C. G. Pedronette y Longin Jan Latecki.  
**Publicación:** *Computer Vision and Image Understanding*, 227, 103618 (2023).  
**DOI/URL:** https://doi.org/10.1016/j.cviu.2022.103618

**Resumen.** Valem et al. proponen Manifold-GCN, un marco que utiliza aprendizaje de variedades basado en rankings para mejorar el grafo de entrada de redes convolucionales sobre grafos (GCN). En vez de construir el grafo únicamente con distancias originales entre características visuales, aplican tres métodos de aprendizaje de variedades —LHRR, RDPAC y BFSTREE— que explotan relaciones de vecindad y similitud contextual. El grafo refinado se combina con cinco arquitecturas GCN y se evalúa en un esquema semisupervisado con solo 10 % de imágenes etiquetadas. El propósito es mejorar la propagación de etiquetas al hacer que la estructura del grafo refleje mejor la geometría intrínseca de la colección.

**Relevancia para el proyecto.** Este trabajo representa claramente la familia basada en variedades y aporta evidencia sobre exactitud bajo escasez de etiquetas. También informa por separado el costo del preprocesamiento de la variedad, el entrenamiento y la prueba, lo que permite una evaluación computacional más transparente que limitarse al tiempo de inferencia.

**Contribuciones clave.**

- Integra métodos de aprendizaje de variedades no supervisados con GCN para clasificación semisupervisada.
- Evalúa sistemáticamente 75 combinaciones de cinco descriptores visuales, tres métodos de variedades y cinco modelos GCN.
- Demuestra que el refinamiento del grafo puede producir mejoras sustanciales cuando la similitud original no representa adecuadamente las relaciones semánticas.
- Separa el tiempo de construcción/refinamiento del grafo de los tiempos de entrenamiento y prueba.

**Métricas y datasets.** Se emplean exactitud, F-measure ponderado y tiempo de ejecución. Los datasets son Flowers17 (1,360 imágenes, 17 clases), Corel5k (5,000 imágenes, 100 clases) y CUB-200-2011 (11,788 imágenes, 200 especies de aves). El protocolo usa diez particiones, con 10 % de ejemplos etiquetados y 90 % no etiquetados; cada partición se ejecuta cinco veces.

**Resultados principales.** En CUB-200-2011, una configuración GCN-APPNP pasa de 55.24 % a 75.59 % de exactitud al incorporar el aprendizaje de variedades. Los mejores resultados reportados por Manifold-GCN alcanzan 97.43 % en Flowers17, 95.57 % en Corel5k y 79.27 % en CUB-200-2011. Sin embargo, en Flowers17 el método WSEF obtiene 97.82 %, lo cual muestra que Manifold-GCN no domina todos los escenarios. El preprocesamiento varía considerablemente: LHRR tarda entre 1.10 y 20.16 segundos según el dataset, mientras RDPAC llega a 104.18 segundos en CUB-200-2011. Los tiempos de entrenamiento de las GCN se mantienen aproximadamente entre 0.14 y 47.8 segundos, y la prueba entre 0.04 y 0.44 segundos en el hardware reportado.

**Limitaciones.** Los experimentos se concentran en grafos k-NN y recíprocos y reutilizan las mismas características para el grafo y la entrada del clasificador. No se estudia el escalamiento a colecciones mucho mayores ni se paralelizan los métodos de variedades. Además, la “robustez” observada corresponde principalmente a la escasez de etiquetas, no a ruido, oclusión, transformaciones de imagen o ataques adversariales.

**Cita clave.** “Our approach is also very efficient and requires very low execution times for training and testing” (Valem et al., 2023, p. 13).

### P02. Dimensionality reduction and classification for hyperspectral image based on robust supervised ISOMAP

**Autores:** Shifei Ding, Christopher A. Keal, Lijuan Zhao y Dan Yu.  
**Publicación:** *Journal of Industrial and Production Engineering*, 39(1), 19–29 (2022).  
**DOI/URL:** https://doi.org/10.1080/21681015.2021.1952657

**Resumen.** Ding et al. presentan Robust Supervised ISOMAP para reducir la dimensionalidad y clasificar imágenes hiperespectrales. El método construye un modelo de credibilidad de las muestras y define una “distancia geodésica triple” que incorpora credibilidad, clase y vecindad. Después utiliza escalamiento multidimensional para obtener el embedding y una red neuronal de regresión generalizada para proyectar y clasificar muestras nuevas. Según el resumen, la propuesta mejora la precisión, la resistencia al ruido y mantiene un tiempo de ejecución viable frente a ISOMAP tradicional.

**Relevancia para el proyecto.** Es el único artículo seleccionado que evalúa explícitamente la resistencia al ruido dentro de una técnica clásica de aprendizaje de variedades. También muestra cómo la supervisión puede modificar la construcción de distancias geodésicas para reducir el efecto de muestras poco confiables.

**Contribuciones clave.**

- Introduce una medida de credibilidad para disminuir la influencia de observaciones ruidosas.
- Combina información de clase, vecindad y credibilidad dentro de la distancia geodésica.
- Incorpora un mecanismo para proyectar muestras fuera del conjunto de entrenamiento, una dificultad habitual de ISOMAP.

**Métricas y datasets.** El resumen identifica precisión de clasificación, comportamiento antirruido y tiempo de ejecución como criterios de evaluación. Los nombres de los datasets, el protocolo experimental, los niveles de ruido y los valores numéricos no pudieron verificarse sin acceso al texto completo; por integridad académica, no se atribuyen datos ausentes.

**Resultados principales.** Los autores afirman que Robust Supervised ISOMAP supera a ISOMAP tradicional en resistencia al ruido y precisión de clasificación, con un costo temporal factible. Esta evidencia debe considerarse cualitativa hasta consultar las tablas y el procedimiento completo del artículo.

**Limitaciones.** Además de la limitación documental indicada, el método necesita etiquetas para construir el embedding, por lo que su comparación con técnicas no supervisadas debe controlar la cantidad de supervisión. Se concentra en imágenes hiperespectrales y no permite concluir que el comportamiento se mantenga en imágenes naturales o médicas. El resumen tampoco permite establecer el orden de complejidad efectivo, el uso de memoria ni la escalabilidad de los cálculos de caminos geodésicos.

**Cita clave.** “The results show that the proposed method has higher anti-noise performance than the traditional one” (Ding et al., 2022, resumen; página no verificable en la versión accesible).

### P03. PHG-Net: Persistent homology guided medical image classification

**Autores:** Yuxin Peng, Hao Wang, Milan Sonka y Danny Z. Chen.  
**Publicación:** *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*, 7583–7592 (2024).  
**DOI/URL:** https://doi.org/10.1109/WACV57701.2024.00741

**Resumen.** PHG-Net integra homología persistente con CNN o Transformers para clasificación de imágenes médicas. El método obtiene diagramas de persistencia mediante complejos cúbicos, los codifica con una red neuronal y utiliza la información topológica para guiar las características visuales. La arquitectura se entrena de extremo a extremo y busca complementar las texturas locales con estructura global. Se evalúa con varias redes base y tres problemas médicos diferentes.

**Relevancia para el proyecto.** El artículo permite analizar la exactitud y el costo marginal de añadir descriptores topológicos a clasificadores visuales modernos. También aporta una observación crítica: las representaciones topológicas aisladas rinden peor que su fusión con características visuales, por lo que el beneficio debe atribuirse a la complementariedad y no a una sustitución completa de la imagen.

**Contribuciones clave.**

- Diseña un codificador aprendible de diagramas de persistencia.
- Introduce un mecanismo de guía topológica compatible con CNN y Transformers.
- Evalúa ablaciones que separan el efecto del diagrama, la guía y el uso compartido de parámetros.
- Reporta parámetros, FLOPs y velocidad de inferencia además de métricas predictivas.

**Métricas y datasets.** Se usan exactitud, AUC, sensibilidad y especificidad, junto con pruebas *t* pareadas. Los datasets son ISIC 2018 (10,015 imágenes de entrenamiento y 193 de validación, siete clases), un conjunto histopatológico de próstata (77 imágenes de lámina completa de 19 pacientes, 5,182 regiones de interés y tres clases) y CBIS-DDSM (1,566 participantes y 6,775 estudios mamográficos). ISIC y próstata se evalúan con validación cruzada de cinco pliegues; CBIS-DDSM usa una división 80/20.

**Resultados principales.** Con SwinV2-B, PHG-Net alcanza 91.92 % en ISIC frente a 90.85 % del backbone, 98.64 % frente a 95.21 % en próstata y 77.23 % frente a 73.51 % en CBIS-DDSM. El modelo base posee 86.913 millones de parámetros y 20.370 GFLOPs, mientras la versión compartida de PHG-Net usa 98.065 millones y 20.796 GFLOPs. El incremento de FLOPs es pequeño, aunque los parámetros aumentan cerca de 12.8 %. La velocidad reportada no empeora en la configuración medida (15.914 FPS frente a 14.937 FPS), pero esta diferencia no debe generalizarse sin controlar implementación, lotes y hardware.

**Limitaciones.** Los experimentos se restringen a imágenes médicas. No se realiza una prueba sistemática con ruido, oclusión, rotación o ataques adversariales, de modo que “robustez” se infiere por consistencia entre datasets y backbones, no por degradación controlada. La arquitectura es híbrida y las mejoras no equivalen a demostrar que un descriptor topológico aislado supera a un embedding geométrico.

**Cita clave.** “Complexity analysis showed that the extra costs introduced by our approach are quite small” (Peng et al., 2024, p. 7591).

### P04. Persistent homology meets object unity: Object recognition in clutter

**Autores:** Ehsan U. Samani y Ashis G. Banerjee.  
**Publicación:** *IEEE Transactions on Robotics*, 40, 886–902 (2024).  
**DOI/URL:** https://doi.org/10.1109/TRO.2023.3343994

**Resumen.** Samani y Banerjee presentan THOR, un sistema de reconocimiento de objetos en escenas desordenadas que usa el descriptor topológico TOPS. A partir de imágenes RGB-D, el objeto segmentado se representa como nube de puntos, se divide en cortes y se calculan características de homología persistente. Estas características alimentan bibliotecas de clasificadores SVM o MLP entrenadas con objetos sintéticos. El método busca preservar la unidad del objeto y funcionar con oclusión, iluminación variable y sensores de profundidad de bajo costo.

**Relevancia para el proyecto.** Es el trabajo con la evaluación de robustez más concreta de la muestra: mide desempeño por nivel de oclusión y en condiciones reales de iluminación y ruido de profundidad. Además, proporciona tiempo extremo a extremo por cuadro, incluyendo segmentación, lo que aproxima mejor el costo operativo.

**Contribuciones clave.**

- Propone TOPS, un descriptor topológico basado en cortes de nubes de puntos.
- Combina homología persistente con un mecanismo de “unidad del objeto” para manejar observaciones parciales.
- Entrena con datos sintéticos y evalúa transferencia al mundo real.
- Publica UW-IS Occluded, un conjunto específicamente diseñado para reconocimiento bajo oclusión.

**Métricas y datasets.** Se emplean exactitud, tiempo por cuadro y validación cruzada. En OCID se usa el subconjunto YCB10 en secuencias desordenadas de hasta diez objetos. UW-IS Occluded contiene 20 clases, 8,456 imágenes de escenas y 42,902 instancias, en ambientes de almacén y sala, iluminación brillante u oscura y tres niveles de oclusión.

**Resultados principales.** En las secuencias inferiores de cámara de OCID, THOR-SVM obtiene 68.88 % y THOR-MLP 66.67 %, frente a 47.33 % de DGCNN y 62.54 % de SimpleView. En UW-IS Occluded, THOR-MLP logra 52.22 % global, mientras DGCNN obtiene 14.58 % y SimpleView 26.43 %. El rendimiento de THOR-MLP disminuye de 51.62 % sin oclusión a 44.26 % con oclusión alta en almacén, y de 56.72 % a 51.88 % en sala. La degradación existe, pero es gradual y cuantificada. El sistema tarda 0.82 segundos por cuadro con seis objetos en un LoCoBot.

**Limitaciones.** THOR depende de una segmentación de instancias previa; la subsegmentación y los falsos positivos perjudican el descriptor. La división en cortes puede distorsionar la geometría y la oclusión extrema puede eliminar cortes completos. Además, explota principalmente forma 3D y no apariencia, por lo que el resultado depende de la calidad del sensor RGB-D y no es directamente comparable con clasificación 2D convencional.

**Cita clave.** “With a prediction speed of 0.82s per frame, THOR operates in real time” (Samani & Banerjee, 2024, p. 15 de la versión de autor).

### P05. Integrating multi-scale and multi-filtration topological features for medical image classification

**Autores:** Pei Gu, Hui Li, Haichao Tang, Daming Xu, Elisa Enriquez, Daeyoung Kim, Bo Fu y Danny Z. Chen.  
**Publicación:** *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*, 8660–8669 (2026).  
**DOI/URL:** https://doi.org/10.1109/WACV61042.2026.00835

**Resumen.** Gu et al. extienden el enfoque de PHG-Net incorporando información topológica a varias escalas y con múltiples filtraciones. Calculan diagramas de persistencia cúbicos en resoluciones de 224, 112 y 56 píxeles y combinan filtraciones de intensidad y gradiente. Un procedimiento tipo *vineyard* relaciona características persistentes entre escalas, y un codificador con atención cruzada integra los descriptores con una CNN o Transformer. El objetivo es capturar simultáneamente estructura global, bordes y estabilidad frente al cambio de escala.

**Relevancia para el proyecto.** Este artículo ofrece el descriptor topológico más elaborado de la selección y evidencia el principal intercambio entre exactitud y costo: ampliar escalas y filtraciones mejora las métricas, pero incrementa parámetros y preprocesamiento. Es especialmente útil para decidir qué costos deben incluirse en una comparación justa.

**Contribuciones clave.**

- Fusiona homología persistente multiescala y multifiltración.
- Utiliza correspondencias entre escalas para priorizar características topológicas estables.
- Compara distancias de emparejamiento y umbrales de estabilidad.
- Reporta ablaciones, número de parámetros y tiempos de cálculo topológico fuera de línea.

**Métricas y datasets.** Se usan exactitud, AUC, sensibilidad y especificidad. Los datasets son ISIC 2018, Kvasir (4,000 imágenes endoscópicas en ocho clases; 2,408/392/1,200 para entrenamiento, validación y prueba) y CBIS-DDSM.

**Resultados principales.** La configuración completa con SwinV2-B alcanza 92.94 % de exactitud y 99.10 % de AUC en ISIC, 81.52 % y 97.25 % en Kvasir, y 78.40 % y 87.22 % en CBIS-DDSM. La variante multiescala aporta en promedio 0.64 puntos porcentuales de exactitud, mientras la multifiltración produce la mayor parte de la ganancia. El costo es importante: el backbone tiene 86.908 millones de parámetros, PHG-Net 94.455 millones y el modelo propuesto 144.238 millones. En Kvasir, la generación de diagramas y los emparejamientos multiescala suman aproximadamente 1 hora y 39 minutos para 4,000 imágenes, aunque se realizan una sola vez fuera de línea.

**Limitaciones.** El modelo aumenta aproximadamente 66 % los parámetros respecto al backbone y más de 50 % respecto a PHG-Net. El preprocesamiento topológico puede convertirse en un cuello de botella al crecer el dataset o la resolución. Los experimentos siguen concentrados en medicina, no incluyen corrupciones controladas y dependen de umbrales de emparejamiento y estabilidad. Por ser una arquitectura híbrida, tampoco constituye una comparación aislada entre representaciones.

**Cita clave.** “PD computation is performed offline, and this process needs to be conducted only once” (Gu et al., 2026, p. 8668).

## 3. Síntesis y análisis comparativo

### 3.1. Relación entre los papers

P01 y P02 comparten la hipótesis de que la estructura de los datos puede describirse mediante relaciones geodésicas o de vecindad. P01 no genera simplemente una proyección bidimensional: refina un grafo que después utiliza una GCN. P02 sí se aproxima al esquema clásico de reducción de dimensionalidad de ISOMAP, pero añade supervisión y credibilidad para resistir muestras ruidosas. En ambos casos, el rendimiento depende de que las vecindades estimadas representen adecuadamente la estructura semántica. Un número de vecinos inadecuado, ruido intenso o “atajos” entre clases pueden deformar las distancias geodésicas.

P03, P04 y P05 no buscan principalmente conservar distancias entre muestras. Extraen invariantes topológicos y luego los vectorizan o codifican. P03 y P05 emplean complejos cúbicos sobre imágenes médicas y fusionan la topología con redes profundas. P04 aplica homología persistente a cortes de nubes de puntos y utiliza clasificadores más sencillos. Los tres respaldan la utilidad de la topología como señal complementaria, pero también muestran que el diseño de la filtración, la vectorización y el clasificador condiciona fuertemente el resultado.

En exactitud, todos reportan mejoras frente a alguna línea base, pero sus porcentajes no deben ordenarse como si provinieran del mismo experimento. Una exactitud de 98.64 % en regiones histológicas no implica superioridad sobre 79.27 % en 200 especies de aves o 52.22 % bajo oclusión robótica. Cambian el número de clases, la dificultad, las particiones, la modalidad, la cantidad de etiquetas y el backbone. La conclusión sostenible es que ambas familias pueden mejorar una representación base cuando su supuesto estructural coincide con el problema.

En robustez, los trabajos usan significados distintos. P01 estudia resistencia a la escasez de etiquetas; P02 declara resistencia al ruido; P04 evalúa oclusión, iluminación, profundidad ruidosa y transferencia sintético-real; P05 modela estabilidad entre escalas; P03 muestra consistencia entre backbones y datasets. Solo P04 ofrece una curva explícita de degradación por severidad de una perturbación observable. Por ello, no sería riguroso afirmar que los descriptores topológicos son globalmente más robustos, aunque P04 sí proporciona la evidencia empírica más fuerte de la muestra para oclusión.

En complejidad, los métodos de variedades suelen pagar por la construcción de vecindades, caminos geodésicos o refinamiento del grafo; los topológicos pagan por construir complejos, calcular persistencia, vectorizar diagramas y, en los modelos híbridos, aumentar parámetros. P01 demuestra que el refinamiento puede ser moderado en conjuntos medianos, pero P05 revela un costo de preprocesamiento que quedaría oculto si solo se informara inferencia. P03 muestra que una integración topológica compacta puede añadir pocos FLOPs, mientras P04 demuestra viabilidad operativa con 0.82 s por cuadro. La comparación correcta debe medir el flujo completo, no únicamente el clasificador final.

### 3.2. Tabla comparativa

| Paper | Familia y representación | Evidencia de exactitud | Robustez realmente evaluada | Evidencia de complejidad | Limitación principal |
|---|---|---|---|---|---|
| P01 Valem et al. (2023) | Variedades; refinamiento de grafo por rankings + GCN | Hasta 97.43 %, 95.57 % y 79.27 % en tres datasets; grandes mejoras en algunas combinaciones | Escasez de etiquetas (10 % etiquetado), no corrupción de imágenes | Preprocesamiento 1.10–104.18 s; tiempos de entrenamiento y prueba separados | No prueba ruido, oclusión ni escala masiva |
| P02 Ding et al. (2022) | Variedades; Robust Supervised ISOMAP | Mejora cualitativa declarada frente a ISOMAP | Ruido mediante credibilidad de muestras | Tiempo descrito como viable, sin cifras verificables en el resumen | Texto completo no accesible; evidencia cuantitativa incompleta |
| P03 Peng et al. (2024) | Topología; diagramas cúbicos + codificador + backbone | Ganancias de 1.07 a 3.72 puntos con SwinV2-B | Generalización entre datasets/backbones, sin estrés por corrupción | 98.065 M vs. 86.913 M parámetros; FLOPs similares | Arquitectura híbrida y solo dominio médico |
| P04 Samani y Banerjee (2024) | Topología; TOPS sobre cortes 3D + SVM/MLP | 52.22 % global en UW-IS; supera baselines 3D estudiados | Oclusión por niveles, iluminación, sensor real y sim-to-real | 0.82 s por cuadro incluyendo segmentación | Depende de segmentación y profundidad RGB-D |
| P05 Gu et al. (2026) | Topología; persistencia multiescala y multifiltración | 92.94 % ISIC, 81.52 % Kvasir y 78.40 % CBIS | Estabilidad estructural entre escalas, no corrupción controlada | 144.238 M parámetros y ~1 h 39 min de preproceso para Kvasir | Alto costo y dependencia de umbrales |

### 3.3. Conexión con nuestro proyecto

La revisión sugiere un experimento controlado en el que la representación sea la variable principal. Para una implementación viable en un curso doctoral, Fashion-MNIST constituye un buen primer dataset real: es suficientemente pequeño para repetir experimentos, presenta diez clases con similitudes visuales y permite construir filtraciones sobre imágenes en escala de grises. Puede añadirse un subconjunto de CIFAR-10 si el tiempo computacional lo permite, pero mezclar dominios no es imprescindible para responder la pregunta inicial.

Se recomienda comparar: (1) una línea base con píxeles normalizados o PCA; (2) un embedding de variedad, por ejemplo ISOMAP y/o UMAP; (3) diagramas de persistencia de complejos cúbicos transformados en imágenes de persistencia; y (4), como análisis opcional, una representación híbrida por concatenación. Para evitar que el clasificador confunda el efecto de la representación, todas las variantes deben alimentar el mismo modelo —regresión logística y, si es viable, SVM con RBF— con idénticas particiones y búsqueda de hiperparámetros. Los transformadores deben ajustarse exclusivamente con entrenamiento para impedir fuga de información.

La exactitud debe evaluarse con *accuracy*, macro-F1, matriz de confusión y media con intervalo de confianza sobre varias semillas. La robustez debe medirse como caída absoluta y relativa de *accuracy* frente al conjunto limpio bajo ruido gaussiano, ruido sal y pimienta, rotaciones, oclusión rectangular y distintos niveles de severidad. La complejidad debe registrar tiempo de ajuste de la representación, tiempo de transformación de entrenamiento y prueba, tiempo del clasificador, memoria máxima, dimensión final y tamaño del modelo. Las visualizaciones pertinentes son embeddings 2D coloreados por clase, ejemplos de diagramas o códigos de barras, curvas de degradación por perturbación y gráficos de tiempo/memoria.

Este diseño responde a la principal debilidad de los papers revisados: ninguno compara directamente una representación de variedad y una topológica usando el mismo dataset, clasificador, particiones, perturbaciones y hardware. Además, permite distinguir tres resultados posibles: mayor exactitud limpia, menor degradación bajo perturbaciones y mayor eficiencia. El método ganador puede ser diferente en cada eje.

## 4. Brechas de investigación

1. **Ausencia de una comparación directa y controlada.** Los cinco artículos comparan sus propuestas con líneas base propias del dominio, pero ninguno enfrenta variedades y descriptores topológicos manteniendo constantes datos, clasificador y presupuesto de ajuste.

2. **Definición inconsistente de robustez.** Escasez de etiquetas, ruido, estabilidad multiescala, oclusión y generalización entre datasets se tratan como fenómenos cercanos, aunque no son equivalentes. Hace falta un protocolo común de corrupciones y severidades.

3. **Contabilidad computacional incompleta.** Algunos estudios informan FLOPs o inferencia y otros tiempo total. Deben incluirse construcción de vecindades, cálculo de persistencia, vectorización, entrenamiento, inferencia, memoria y costo de selección de hiperparámetros.

4. **Confusión entre representación y clasificador.** P01 utiliza GCN y P03/P05 redes profundas híbridas. Las mejoras pueden provenir de la interacción con el clasificador. Una evaluación con un clasificador idéntico permitiría aislar el valor de cada descriptor.

5. **Concentración en dominios especializados.** Tres artículos se centran en medicina, uno en hiperespectral y otro en robótica RGB-D. Se necesitan pruebas en un benchmark 2D común antes de generalizar conclusiones.

6. **Escalabilidad insuficientemente estudiada.** ISOMAP y la homología persistente pueden crecer rápidamente con el número de muestras, la resolución o el tamaño del complejo. Son necesarios experimentos de escalamiento y medición de memoria.

7. **Poca evaluación estadística y de reproducibilidad.** No todos los trabajos reportan intervalos, múltiples semillas, código o sensibilidad completa a hiperparámetros. Las diferencias pequeñas podrían depender del procedimiento experimental.

## 5. Referencias

Ding, S., Keal, C. A., Zhao, L., & Yu, D. (2022). Dimensionality reduction and classification for hyperspectral image based on robust supervised ISOMAP. *Journal of Industrial and Production Engineering, 39*(1), 19–29. https://doi.org/10.1080/21681015.2021.1952657

Gu, P., Li, H., Tang, H., Xu, D., Enriquez, E., Kim, D., Fu, B., & Chen, D. Z. (2026). Integrating multi-scale and multi-filtration topological features for medical image classification. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision* (pp. 8660–8669). https://doi.org/10.1109/WACV61042.2026.00835

Peng, Y., Wang, H., Sonka, M., & Chen, D. Z. (2024). PHG-Net: Persistent homology guided medical image classification. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision* (pp. 7583–7592). https://doi.org/10.1109/WACV57701.2024.00741

Samani, E. U., & Banerjee, A. G. (2024). Persistent homology meets object unity: Object recognition in clutter. *IEEE Transactions on Robotics, 40*, 886–902. https://doi.org/10.1109/TRO.2023.3343994

Valem, L. P., Pedronette, D. C. G., & Latecki, L. J. (2023). Graph convolutional networks based on manifold learning for semi-supervised image classification. *Computer Vision and Image Understanding, 227*, 103618. https://doi.org/10.1016/j.cviu.2022.103618

## Declaración sobre el uso de inteligencia artificial

Se utilizó una herramienta de inteligencia artificial como apoyo para organizar la evidencia extraída, comparar los artículos y revisar la redacción. La selección final, la verificación de los datos disponibles y la responsabilidad sobre la interpretación académica corresponden al autor del trabajo. Antes de entregar la versión definitiva, se recomienda contrastar cada referencia con el PDF institucional y adaptar esta declaración a la política del curso
