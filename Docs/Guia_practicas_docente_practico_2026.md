# Guía de prácticos para el docente de prácticas — SIG III 2026

Este documento es un insumo de coordinación entre Felipe Sodré Mendes Barros (teoría, asincrónica) y
Demian Lorán (práctica, presencial), a partir de lo que planteó Demian por mail: para cada práctico, saber
qué necesita aprender el alumno y qué no conviene resolverle, y contar con un criterio compartido para
explicar cada actividad con un ejemplo distinto al que el alumno debe resolver.

La información de cada clase sale de cruzar tres fuentes: el texto correspondiente en
`Cuadernillo de catedra/antiguos/`, la presentación de `Clases/antiguos/` y el cronograma de
`Docs/Plan_detallado_clases_SIG_III.xlsx` / `Docs/Planificacion SIG III 2026.docx`. La columna "Novedades
2026" sale de `diagnostico_textos.md` y describe **intención de reescritura**, no contenido ya escrito —
donde el texto todavía no exista, se aclara. Los "ejemplos alternativos" son sugerencias de partida para
que Demian las ajuste con su propio criterio, no la única opción válida.

## Postura para la respuesta a Demian

Notas de Felipe sobre los otros dos puntos del mail, para usar como base de la respuesta (no son texto
definitivo, quedan para que Felipe las revise antes de mandarlas):

Sobre el formato de devolución: tiene sentido la propuesta de Demian de un video informal comentando la
presentación de cada clase, en vez de duplicar el mismo contenido en una nota escrita — es más rápido de
producir del lado de Felipe y deja abierta la posibilidad de que Demian responda con su propia devolución
en un ida y vuelta liviano, sin la carga de una reunión sincrónica.

Sobre dividir los videos de práctica en uno previo al desafío y otro remedial posterior: separar ambos
momentos tiene sentido y encaja con el patrón semanal que ya usa la materia (texto → presentación →
desafío/cuestionario, ver `CLAUDE.md`), y con el modelo que se está evaluando para 2026 de separar más
nítidamente lo conceptual asincrónico de la práctica en clase. El video previo debería limitarse a
encuadrar la actividad y el objetivo de aprendizaje, sin resolver el desafío (ver columna "Qué NO debe
resolvérsele" de cada clase, más abajo); el remedial se graba después de que el alumno ya intentó
resolver, mostrando los errores más frecuentes de esa cohorte en particular en vez de repetir la
explicación inicial.

## Clases con práctica (Semana 1 a 12)

### Semana 1 — Introducción al curso / estructura de datos ráster
*(pptx `0_Introducción_curso`; Texto I – Introducción a los Datos Ráster)*

- **Qué debe aprender el alumno**: qué es un dato ráster (matriz de celdas con valor + resolución +
  extensión + sistema de referencia), en qué se diferencia estructuralmente de un vector, qué tipos de
  información puede almacenar (continua, categórica, temática) y de dónde provienen los ráster que va a
  usar en la cursada (SRTM, ALOS PALSAR, Sentinel-2, Landsat, MODIS, cartografía temática, productos
  derivados como NDVI/NDWI/pendiente).
- **Qué NO debe resolvérsele**: esta primera semana no tiene un desafío técnico propio (es una clase
  institucional + arranque del foro), así que no hay riesgo de "resolver" nada — el punto de atención acá
  es no darle ya armada la respuesta del foro ("¿qué características tienen los datos ráster? ¿cómo los
  usamos?"), que es una reflexión que el alumno tiene que elaborar con lo ya visto en SIG I/II y PDI.
- **Ejemplo alternativo sugerido**: no aplica (no hay ejercicio técnico esta semana).
- **Novedades 2026**: la versión `.qmd` nueva de Texto I ya resolvió sus puntos débiles (interconversión
  vector↔ráster desarrollada, sección de beneficios/debilidades, cuidados prácticos con tabla de
  atributos/metadatos); el catálogo de formatos ráster queda deliberadamente para Texto VIII.

### Semana 2 — Rasterización
*(pptx `1_Rasterización`; Texto II – Rasterización de datos vectoriales)*

- **Qué debe aprender el alumno**: Considerando que ellos ya conocen e ya han trabajado con imágenes de satelite y MDE, la idea es mostrarles otra forma de producir un raster: a partir de datos vectoriales ya existentes, a partir del proceso de rasterización. Lo importante es que quede claro a ellos las cuatro decisiones (técnicas) que definen un proceso de rasterización y por qué ninguna de esas decisiones es neutra:
  * qué valor asignarle a cada píxel: ¿binario o catogorico acorde a alguna columna numerica de la table de atributos? Cada uno "contesta" a preguntas distintas; 
  * qué resolución espacial usar: Se la podemos definir de dos maneras, definiendo la cantidad de celdas en alto y largo o, como veremos en otra clase, por el tamaño del píxel);
  * qué extensión darle al ráster de salida: Por defecto se usa la extensión del dato raster. Pero se puede alterar, de ser necesario. Lo importante es que ellos entiendas que, como informamos la resolución espacial por cantidad de celdas, recién ahora, al infomrar la extensión es que podríamos clacular el tamaño del píxel.;
  * cómo tratar el valor NoData: En este punto hay algo importante. El ráster es una matriz regular, por más que hagan el recorte a una región de trabajo y no veamos a los pixeles externos a dicha área, no quiere decir que dichas celdas no exiten. Ellas existen y están configuradas como NoData, haciendo con que los SIGs se las reconozcan y no se la presenten; Ese punto es importante no solo por cuestiones visuales. Si no que, como veremos más adelante, an trabajar con algebra de mapas, cualquier operación matemática sobre pixeles "NoData" retorna valores "NoData".

Ellos deberán hacer de vuelta la operación, pero con otros datos;
- **Desafío**: 
 * ¿Qué criterio usa QGIS para identificar cuando una celda representará o no una geometría rasterizada? - Que aprendan a buscar infomraciones más tecnicas en paginas de documentación
 * Ocupando el dato “polígonos_superpuestos”, identificar ¿cómo quedará rasterizado el área de superposición al usar el campo id como valor a ser asignado al raster? - Que pruepben y sean capaces de identificar algunas situaciones límite en la conversión vector-> raster

### Semana 3 — Álgebra de mapas
*(pptx `2_Análisis_raster_algebra_mapas`; Texto III – Álgebra de mapas)*

- **Qué debe aprender el alumno**: La diferenciaa entre QGIS y Gdal; búsqueda de detalles en la página de documentación; Definición de la resolución espacial a partir de la cantidad de píxeles avidenciando el calculo.
- En un nuevo proyecto: Usamos el ejemplo de inundación en Bahi Blanca como tema para realizar algebra de mpaas entre pendiente y uso de suelo. Revisa qué es el álgebra de mapas y sus usos típicos; Enseña a manejar la calculadora ráster de QGIS con su sintaxis. Al concluir la actividad se presenta el problema concreto de sumar capas categóricas sin ponderar lo que impide identificar la trazabilidad o que distintas combinaciones llevan a un mismo valor aunque no deban; Se les deja el desafío de ponderar para, en las filminas siguientes, presentarles la solución.

### Semana 4 — Análisis monocriterio
*(pptx `3a_Análisis_texto_Buzai` + `3b_Análisis_raster_monocriterio`; Texto IV – Artículos científicos y discurso referido + Texto V – Calculadora Ráster en QGIS) - Operaciones binarias/booleanas (==, !=, <,>, etc)*

- **Qué debe aprender el alumno**: por el lado de Texto IV, a leer e interpretar artículos científicos (estructura IMRyD, uso del discurso referido) tomando como caso el capítulo de Buzai sobre Evaluación Multicriterio (EMC); por el lado del texto de Buzai, una introducción al Análisis Multi Critério ("POTENCIALIDAD DE LA METODOLOGÍA DE EVALUACIÓN MULTICRITERIO APLICADA CON SISTEMAS DE INFORMACIÓN GEOGRÁFICA"); En un proyecto qGIS realizar un análisis monocriterio (cálculos aritméticos) para instalación de energía solar en Misiones. Desafío es que los estudiantes ya entiendan que deberán preprocesar el MDE, proyectandolo para que el calculo de pndiente ande bien (reproyección a POSGAR faja 7, cálculo de pendiente). Al final de la clase se presentan las operaciones de conyncción disynccion y planteael desafío que agregar una variable más (orientación), que será abordado en la proxima clase.
Les queda un cuestionario con ejempplos de operaciones monocriteiro

### Semana 5 — Análisis multicriterio
*(pptx `4a_Analisis_multicriterio` + `4b_Analisis_multicriterio`; Texto V – La Calculadora Ráster en QGIS, apartados de AND/OR/NOT — el contenido operativo que tenía el `Texto VI - Operaciones lógicas mono- y multicriterio.docx` de `antiguos/` se mudó ahí al reescribirlo como `.qmd`; Texto VI queda reservado para métodos avanzados de EMC — Fuzzy, Bayesiano, Redes Neuronales — cuando se reescriba)*

- **Qué debe aprender el alumno**: operaciones lógicas elementales y compuestas (AND/OR/NOT) sobre dos rásteres (pendiente y orinetación) y, despues de realizarlas se agrega otra más - distancia de las rutas - que demandará preprocesamiento - Rasterizar -> retomando las clases inciales. La resolución está en la presentación 4b, en la cual se profundiza más tecnicamente las propiedades de un raster.
Les queda cuestionario multicriterio apra desarerollar

### (Semana 6 — Parcial I: ver apartado de Parciales, más abajo)
Atención ya que el año pasado tuvimos algunas interpretaciones distintas al como deberpia ser la operación. Anque no hayan comprometido al objetivo inicial de que ellos demuestren saber usar calculadora raster y operaciones ya presentadas.

### Semana 7 — Alineación y remuestreo de ráster
*(pptx `5_Alinear_raster`; Texto VII – Alineación_Interpolación)*

- **Qué debe aprender el alumno**: Revisa parcial I (quizás no haga falta); Retoma el proyecto anterior y agrega a la variable de uso del suelo, para abordar el por qué rásteres de distinto origen pueden no estar alineados (distinta resolución, extensión o grilla). lES MUESTRA QUE SÍ, SE PUEDE TRABAJAR CON RASTERS NO ALINEADOS, pero no se debe ya que perdemos el contrón de qué celda esta siendo calculada con qué celda... Presenta la herramienta de alinear rásteres, y los tres métodos de remuestreo — vecino más próximo, bilineal y cúbico — y cuándo conviene cada uno según si la capa es categórica o continua. Presenta los principales algoritmos. Remota la actviidad proponiendo agregar jerarquización de clases de uso. Aborda la diferencia entre la oopración aritmetica y la logica, como reflexion final. 

### Semana 8 — Estadística zonal, filtrado Sieve y compresión/pirámides
*(pptx `6_EstadisticaZonal_Sieve`; Texto VIII – Compresión y pirámides)*

- **Qué debe aprender el alumno**: Sigue el proyecto anterior y agrega un problema más, limmitar las áreas indicadas aal menos 4 hectareas; Presenta el uso del filtrado (sieve) , ya usado para remoción del efecto "sal y pimienta"de  clasificación para solicionaarlo. Como el resultado no tiene configurado pixeles NoData, aprovecho para usar la herramienta de exportación para abordar el uso de la compresión de raster y explicarlos (con/sin pérdida, formatos como BigTIFF,  PACKBITS, Deflate, JPEG) y pirámides/overviews (niveles, métodos de remuestreo, cuándo conviene cada  configuración) — con foco en cómo estas decisiones técnicas afectan tanto el análisis como la  visualización. Plantea como desafío el calculo de área usando raster.
Ese desafío no tiene su solucion presentada. Basicamente se debería usar estadística zonal.

### Semana 9 — Interpolación
*(pptx `7_Interpolación`; sin texto propio en el Cuadernillo — ver nota abajo)*

- **Qué debe aprender el alumno**: Se ocupo otro proyecto. Vuelve a la rasterización para discutir que sí, se puede rasterizar datos vectoriales (principalmente de puntos) usando otros abordajes más allá de la herramienta rasterización, o sea, a partir de la interporlación. CLARO, la "pregunta" es otra. Pero puede ser entendido también como una manera de conversión de información vectorial a raster....
Presenta la diferencia entre rasterizar puntos e interpolar, el método de  vecino más cercano, la primera ley de la geografía como fundamento de la interpolación espacial, interpolación lineal y distancia inversa ponderada (IDW).; discute algunos de estos abordajes cond atos vectoriales tb. Les deja como desafío probar otros algoritmos;

### Semana 10 — Filtros de ráster / ventana móvil (operaciones focales)
*(pptx `8_FiltrosRaster_MovingWindow`; Texto IX – Operaciones focales)*

- **Qué debe aprender el alumno**: el pasaje de operación vertical (álgebra de mapas, celda a celda) a operación de vecindad (estadística focal); Definciones básicas: qué es una máscara/kernel y los tipos de vecindad, los tipos de funciones focales, en qué se diferencia esto del filtrado de PDI, el efecto del tamaño de ventana sobre el resultado; Se trabaja sobre un caso de calcular cantidad de forestación en el radio de 1Km.

### Semana 11 — Digitalización y georreferenciación
*(pptx `9_Digitalización y Georreferenciación`; sin texto propio en el Cuadernillo)*

- **Qué debe aprender el alumno**: el proceso de georreferenciar cartografía digitalizada con el Georreferenciador de QGIS, la lógica de puntos de control terrestre y la configuración de la transformación, tomando como caso el mapa geológico de Misiones de 1999.

### Semana 12 — Métricas de paisaje
*(pptx `11_Metricas_de_paisaje`; Texto X – Métricas de paisaje)*

- **Qué debe aprender el alumno**: El uso de ráster para cálculos de metricas de paisaje con LecoS (qué es un paisaje y el modelo Parche-Corredor-Matriz, las métricas de paisaje en sus tres niveles (Landscape, Class, Patch).

## Parciales I y II

Los parciales ya tienen consigna y rúbrica propias (`Evaluacion_Parcial_I.docx` +
`RubicaEvaluacion_Parcial_I.docx`; `EvaluacionParcial_II.docx` con su propia rúbrica embebida).

**Parcial I** (análisis multicriterio de aptitud productiva en Misiones, con capas climáticas WorldClim para 8 sistemas productivos): el acompañamiento durante el parcial debe limitarse a soporte técnico de herramienta (dudas de manejo de QGIS/calculadora ráster), no a decidir qué umbrales usar ni qué capas combinar — eso es lo que evalúa la rúbrica. Al final del año pasado revisamos al cursada y reconocemos que el principal obstáculo fue el manejo de muchas capas y su preprocesamiento, no el concepto de multicriterio en sí.

**Parcial II** (mismo caso bajo proyecciones climáticas CMIP6, comparación algebraica actual-vs-futuro). Muchos alumnos se quedaron en técnicas clásicas (declividad, NDVI) y subutilizaron interpolación y filtros.
