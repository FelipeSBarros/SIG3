# Diagnóstico: planificación SIG III 2026 y textos del Cuadernillo de cátedra

Revisión de `Docs/` (planificación, plan detallado de clases) y de los diez textos de
`Cuadernillo de catedra/`, con foco en qué se podría mejorar o agregar en cada tema. Incluye también los
puntos de `Reflexiones SIG 3 2025.docx` cuando explican por qué conviene un ajuste puntual.

## Hallazgo transversal: hay temas de clase sin texto propio en el Cuadernillo

Cruzando el cronograma de `Clases/` (12 clases, 0–10 + entrega de TP II) contra los diez textos (`Texto
I`–`Texto X`), quedan temas del programa **sin texto dedicado**:

- **Clase 6 — Estadística Zonal / Sieve**: no tiene texto en el Cuadernillo.
- **Clase 9 — Digitalización y Georreferenciación**: no tiene texto en el Cuadernillo.
- **Clase 7 — Interpolación**: `Texto VII - Alineación_Interpolación.docx` cubre en realidad **remuestreo
  y alineación** (vecino más próximo, bilineal, cúbico) — no la interpolación espacial punto→superficie
  (IDW, Kriging, Spline/TIN) que promete tanto el nombre de la clase como la bibliografía que cita el plan
  detallado ("INTERPOLACIÓN ESPACIAL CON SISTEMAS DE INFORMACIÓN GEOGRÁFICA"). Este es, probablemente, el
  gap más importante: `Reflexiones SIG 3 2025.docx` señala que los alumnos subutilizaron interpolación en
  el segundo parcial, y el Cuadernillo nunca llega a desarrollarla como tal.
- **Modelos de costo** y **Modelo de elevación y de superficie**: figuran explícitamente en los
  "Contenidos mínimos" y en la Unidad II de `Planificacion SIG III 2026.docx`, pero no tienen texto propio
  (solo se mencionan de pasada en Texto I).
- **Reclasificación**: también aparece en los contenidos mínimos, sin tratamiento dedicado en ningún
  texto.

Recomendación general: antes de seguir profundizando temas ya bien cubiertos, priorizar estos huecos —
en particular interpolación espacial, que además está respaldada por la retroalimentación de 2025.

## Revisión tema por tema

### Texto I — Introducción a los Datos Ráster
**Actualizado (2026-08-11): los cuatro puntos débiles señalados originalmente ya están resueltos** en
`Cuadernillo de catedra/nuevos/Texto I – Introducción a los Datos Ráster.qmd`. Buena base conceptual —qué es un ráster,
estructura, tipos de dato (continuo/categórico, con la terminología grade regular/matriz temática),
mono/multibanda (con el gancho a espacios celulares y cubos de datos), las cuatro resoluciones, y el marco
formal geo-campo/geo-objeto sumado en la revisión con los libros del INPE— y además:
- La interconversión vector↔ráster tiene ahora una sección propia y desarrollada ("Interconversión entre
  vector y ráster"), con rasterización y vectorización, dos figuras y remisión al Texto II.
- Existe una sección dedicada "Beneficios y debilidades del modelo ráster".
- **El problema de la tabla de atributos inexistente ya tiene tratamiento propio**, en la sección
  "Cuidados prácticos al manipular archivos ráster": nomenclatura de archivos, estructura de carpetas,
  metadatos y archivos auxiliares (`.aux.xml`, `.tfw`, `.ovr`, con GeoTIFF como ejemplo) y la idea de
  bitácora de procesamiento.

El único punto pendiente es menor y deliberado: Texto I no da un catálogo completo de formatos ráster
(GeoTIFF, IMG, ASCII grid) — eso se dejó a propósito para el Texto VIII ("Compresión y pirámides"), que ya
lo cubre en profundidad y al que Texto I remite explícitamente al cierre. No correspondería duplicarlo.

### Texto II — Rasterización de datos vectoriales
Sólido y muy práctico: valor de píxel (campo vs. valor fijo), resolución en QGIS, extensión, y una muy
buena sección sobre NoData y sus riesgos. Podría sumar un apartado sobre el camino inverso —
ráster→vector (poligonización/vectorización) —, que hoy no tiene desarrollo dedicado en ningún texto del
Cuadernillo (sí se lo menciona brevemente en Texto I).

### Texto III — Álgebra de mapas
Sólido, con buena conexión con lo ya visto en Procesamiento Digital de Imágenes (NDVI, ΔNDBI) y ejemplos
de jerarquización/ponderación bien explicados (incluye la trampa de sumar categorías sin multiplicar por
10/100). Podría cerrar con un puente explícito hacia la variedad de técnicas disponibles en la Unidad II
(no quedarse en NDVI/declividad), anticipando el punto que aparece con fuerza en Reflexiones 2025.

### Texto IV — Artículos científicos y discurso referido
Bien escrito y claro (estructura IMRyD, funciones del discurso referido), pero genérico: no tiene ningún
ejemplo del dominio ráster/SIG. Podría sumar un ejemplo de discurso referido citando alguno de los papers
ya usados en Texto IX o X (McGarigal et al. 2012, Miller & Thode 2007, Wilson & Gallant 2000), para anclar
la destreza de lectura académica a la disciplina.

### Texto V — Calculadora Ráster en QGIS (funciones trigonométricas y lógicas)
Contenido útil (aritmética, trigonométricas, condicionales con máscaras), pero:
- Tiene un error de redacción: la sección 1 dice "ya hemos visto operaciones trigonométricos entre
  imágenes raster" cuando en realidad describe operaciones **aritméticas**.
- Podría ampliarse con funciones estadísticas (`min`, `max`, `sum` entre capas) y la sintaxis `if()`
  explícita de la Calculadora Ráster, hoy ausente pese a ser muy usada en clase.

### Texto VI — Operaciones lógicas mono- y multicriterio sobre rásteres
Muy completo: operadores de comparación, AND/OR/NOT, relación con teoría de conjuntos, requisitos de
alineamiento entre capas, diferencia entre combinar con `+` (jerarquización) y con `AND` (filtro estricto),
y buenas prácticas al cierre. Es el texto de mejor nivel del Cuadernillo — un buen modelo a imitar en
estructura para los demás.

### Texto VII — Alineación_Interpolación
Como se señaló en el hallazgo transversal, es el gap más importante: solo cubre remuestreo/alineación
(vecino más próximo, bilineal, cúbico), no interpolación espacial real a partir de puntos (IDW, Kriging,
Spline/TIN). Recomendación: dividir en dos piezas — mantener esta como "Alineación y remuestreo de
ráster", y sumar un texto nuevo de "Interpolación espacial" que si cubra la clase 7 tal como está en el
programa.

### Texto VIII — Compresión y pirámides
Muy completo y bien estructurado: compresión con/sin pérdida, algoritmos (PACKBITS, LZW, Deflate, ZSTD,
LZMA, JPEG, LERC), pirámides/overviews, tipos de archivo piramidal, cuándo usar cada configuración. Sin
brechas relevantes.

### Texto IX — Estadística focal y Moving Window
Excelente: buena progresión conceptual (de operación vertical a focal), tipos de máscara/kernel,
diferencia máscara/kernel/convolución con fórmula explicada, efectos del tamaño de ventana y del borde, y
tres ejemplos científicos reales citados con referencia bibliográfica. Nivel de referencia para el resto
del Cuadernillo.

### Texto X — Métricas de paisaje
Excelente y crítico: no solo presenta las métricas (SHDI, CONTAG, PLAND, cohesión, área, forma), sino que
dedica una sección entera a limitaciones (dependencia de la definición del paisaje, efectos de borde,
redundancia entre métricas, falta de marco de referencia). Sin brechas relevantes.

## Nota transversal de forma

Varios textos tienen interferencias del portugués o errores de tipeo ("haciendo con que", "endiformato",
"própia", "teçnica", "supuesto... arbitrária", "comple"). No es urgente, pero conviene una pasada de
corrección lingüística conjunta sobre todo el Cuadernillo en algún momento de la revisión 2026.

## Priorización sugerida

1. **Interpolación espacial real** (IDW/Kriging/Spline) — gap más grande, respaldado por Reflexiones 2025.
2. **Texto I ampliado** (ver `Cuadernillo de catedra/nuevos/Texto I – Introducción a los Datos Ráster.qmd`; los puntos débiles
   originalmente señalados ya están resueltos — ver nota de 2026-08-11 en la revisión tema por tema).
3. Textos nuevos para Estadística zonal/Sieve, Digitalización/Georreferenciación, Modelos de costo,
   Modelo de elevación/superficie, Reclasificación.
4. Ajustes menores en Textos II, III, IV, V (apartados y ejemplos puntuales, detallados arriba).
5. Pasada de corrección lingüística transversal.

## Fuentes nuevas: libros del INPE (agregados a Bibliografía el 2026-08-10)

Se sumaron tres PDFs a `Bibliografia/` que resultaron ser capítulos de dos obras del INPE:

- `cap6-dinamica.pdf` y `cap9-inferencia.pdf` son en realidad los **capítulos 8 y 9** del libro colectivo
  *Introdução à Ciência da Geoinformação*, editado y organizado por Gilberto Câmara, Clodoveu Davis y
  Antônio Miguel Vieira Monteiro (INPE, 2001), accesible en
  <http://www.dpi.inpe.br/gilberto/livro/introd/>: "Modelagem Dinâmica e Geoprocessamento" (Pedrosa y
  Câmara) e "Inferência Geográfica e Suporte à Decisão" (Moreira, Barbosa, Câmara y Almeida Filho),
  respectivamente.
- `TutorialBdGeo_GeoBrasil2006.pdf` es el "Tutorial sobre Bancos de Dados Geográficos" (Queiroz y Ferreira,
  INPE/GeoBrasil 2006), con el marco formal geo-campo/geo-objeto y la representación matricial
  (grade regular, matriz temática, espacios celulares).

El tutorial ya se incorporó a **Texto I** (`Cuadernillo de catedra/nuevos/Texto I – Introducción a los
Datos Ráster.qmd`, citado como `@queiroz2006tutorial`): formaliza la distinción vector/ráster con
geo-campo/geo-objeto en "¿Qué son los datos ráster?", ancla continuo/categórico a la terminología
grade regular/matriz temática en "Tipos de datos que pueden almacenar", y deja un gancho hacia espacios
celulares y cubos de datos espacio-temporales en el mismo apartado (multibanda).

Los capítulos 8 y 9 del libro de Câmara et al., en cambio, no encajan en el alcance de Texto I (que es
introductorio) y quedan pendientes para cuando se aborden sus temas propios:

- **Cap. 9 (Inferência Geográfica)** — cubre Booleano, Media Ponderada, Fuzzy, Bayesiano y Redes
  Neuronales para combinar evidencias espaciales. Es la fuente de peso para cuando se reescriba
  **Texto VI** (hoy "Operaciones lógicas mono- y multicriterio") como `.qmd`: responde directamente al
  hallazgo de `Reflexiones SIG 3 2025.docx` de que los alumnos se quedaron en técnicas clásicas
  (declividad, NDVI) y subutilizaron el repertorio completo de la unidad — Fuzzy y Bayesiano en particular
  amplían ese texto más allá de Booleano/Media Ponderada, que es donde hoy se detiene.
- **Cap. 8 (Modelagem Dinâmica)** — cubre modelado dinámico espacio-temporal y autómatas celulares. Es la
  fuente natural para un futuro texto de modelado dinámico/espacio-temporal, todavía sin lugar propio en
  el Cuadernillo, que conectaría con "cubos de datos" de la Unidad III y con el notebook
  `Clase_X_Análisis_espacio_temporal_Cubo_de_Datos.ipynb` de `Actividades prácticas/`.

## Tabla resumen

Condensa la revisión tema por tema de arriba, cruzada con los contenidos mínimos y el cronograma de
`Docs/Planificacion SIG III 2026.docx`. El detalle largo de cada punto sigue viviendo en las secciones en
prosa; esta tabla es solo un mapa rápido para priorizar.

| Texto | Clase correlativa | Qué debería cubrir | Qué cubre hoy | Qué falta agregar |
|---|---|---|---|---|
| **Texto I** – Introducción a los Datos Ráster | Clase 1 (Rasterización, parte introductoria) | Características, propiedades y relevancia de la estructura ráster (Unidad I) | Qué es un ráster, estructura, tipos de dato, cuatro resoluciones, fuentes de datos, marco geo-campo/geo-objeto (ampliado con INPE), interconversión vector↔ráster desarrollada, beneficios/debilidades dedicados, y cuidados prácticos (tabla de atributos, nomenclatura, archivos auxiliares) | Sin brechas relevantes — remite a Texto VIII para el catálogo completo de formatos |
| **Texto II** – Rasterización de datos vectoriales | Clase 1 (Rasterización, parte técnica) | Métodos y procesos de creación de ráster (Unidad II) | Valor de píxel (campo/valor fijo), resolución, extensión, NoData | Vectorización (camino inverso ráster→vector), sin desarrollo dedicado en ningún texto |
| **Texto III** – Álgebra de mapas | Clase 2 (Álgebra de mapas) | Conceptos y fundamentos del modelado espacial (Unidad II) | Operaciones celda a celda, jerarquización/ponderación, NDVI/ΔNDBI | Puente explícito hacia el resto de técnicas de la Unidad II, para no quedarse en NDVI/declividad (Reflexiones 2025) |
| **Texto IV** – Artículos científicos y discurso referido | Clase 3a (Análisis de texto/Buzai) | Lectura académica aplicada al dominio ráster/SIG | Estructura IMRyD, funciones del discurso referido (bien explicado, pero genérico) | Ejemplo propio del dominio ráster/SIG (p. ej. citando papers ya usados en Texto IX/X) |
| **Texto V** – Calculadora Ráster en QGIS | Clases 3b/4 (mono/multicriterio, uso de calculadora) | Manipulación de ráster: cálculos (Unidad II) | Aritmética, trigonométricas, condicionales con máscaras | Corregir error de redacción ("trigonométricas" en la sección de aritmética); sumar funciones estadísticas (`min`/`max`/`sum`) y sintaxis `if()` explícita |
| **Texto VI** – Operaciones lógicas mono- y multicriterio | Clases 3b/4 (mono/multicriterio) | Análisis ráster mono y multicriterio (Unidad III) | Comparación, AND/OR/NOT, teoría de conjuntos, alineamiento, jerarquización vs. filtro — texto de mejor nivel del Cuadernillo | Nada urgente; candidato a sumar Fuzzy/Bayesiano/Redes Neuronales (cap. 9 INPE) cuando se reescriba como `.qmd` |
| **Texto VII** – Alineación_Interpolación | Clases 5 (Alinear ráster) y 7 (Interpolación) | Alineación/remuestreo **y** interpolación espacial (IDW, Kriging, Spline/TIN) (Unidad II) | Solo remuestreo/alineación (vecino más próximo, bilineal, cúbico) | Interpolación espacial real — gap más importante del Cuadernillo, respaldado por Reflexiones 2025; dividir en dos textos |
| **Texto VIII** – Compresión y pirámides | Sin clase dedicada en el cronograma (contenido de referencia) | Manipulación de ráster: formatos y compresión (Unidad II) | Compresión con/sin pérdida, algoritmos (PACKBITS, LZW, Deflate, ZSTD, LZMA, JPEG, LERC), pirámides/overviews | Sin brechas relevantes |
| **Texto IX** – Estadística focal y Moving Window | Clase 8 (Filtros ráster / Moving Window) | Manipulación de ráster: filtros (Unidad II) | Máscara/kernel/convolución, tamaño de ventana, efectos de borde, ejemplos científicos citados | Sin brechas relevantes — nivel de referencia del Cuadernillo |
| **Texto X** – Métricas de paisaje | Clase 10/11 (Métricas de paisaje) | Análisis de paisaje (Unidad III) | Métricas (SHDI, CONTAG, PLAND, cohesión, área, forma) y sección crítica de limitaciones | Sin brechas relevantes |
| *(sin texto)* | Clase 6 — Estadística Zonal / Sieve | Manipulación de ráster: estadística zonal (Unidad II) | Nada | Texto completo |
| *(sin texto)* | Clase 9 — Digitalización y Georreferenciación | Adquisición de datos | Nada | Texto completo |
| *(sin texto)* | Sin clase propia — Unidad II, contenidos mínimos | Modelos de costo | Mención de pasada en Texto I | Texto completo |
| *(sin texto)* | Sin clase propia — Unidad II, contenidos mínimos | Modelo de elevación y de superficie | Mención de pasada en Texto I | Texto completo |
| *(sin texto)* | Sin clase propia — Unidad II, contenidos mínimos | Reclasificación | Solo tangencial en Texto VI | Texto completo |
