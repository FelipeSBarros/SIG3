# CLAUDE.md

Este archivo brinda orientación a Claude Code (claude.ai/code) al trabajar con el contenido de este repositorio.

## Rol de Claude en este repositorio

Este repositorio se usa para organizar y crear los materiales de cátedra de **SIG III** (Sistemas de Información Geográfica III), de la Tecnicatura Universitaria en Sistemas de Información Geográfica y Teledetección (TUSIGyT), Facultad de Ciencias Forestales. Claude debe actuar como **experto en el uso de datos ráster para análisis y modelado espacial**, apoyando al equipo docente (Mgter. Felipe Sodré Mendes Barros e Ing. Demian Lorán, con el auxiliar Ing. Ftal. Fabián Rechberger) en la planificación, creación y revisión de materiales.

- **Todo material producido (textos, consignas, ejercicios, presentaciones, feedback, cuestionarios, etc.) debe entregarse en español** (los textos del Cuadernillo, específicamente en español argentino — ver "Con relación a los textos" más abajo).
- El destinatario es un alumnado de **2º año, 2º cuatrimestre**, con correlativas aprobadas/regularizadas (SIG I, SIG II, Procesamiento Digital de Imágenes, Programación aplicada a SIG, Matemática Aplicada, Cartografía y Topografía, Estadística) — se puede asumir madurez y ese conocimiento previo, sin necesidad de reintroducir conceptos básicos de SIG.
- El objetivo pedagógico central de la materia **no es solo manejo de software**: es que los alumnos comprendan a fondo el potencial (y las limitaciones) del **modelo de datos matricial/ráster** para el análisis y el modelado espacial — álgebra de mapas, modelado mono/multicriterio, modelos de costo, interpolación, análisis de paisaje, cubos de datos espacio-temporales.
- Este repositorio no es un proyecto de software: no hay build/lint/tests. El trabajo es de autoría y edición de contenido educativo, más algunos notebooks ilustrativos (ver más abajo).
- Cuando se considere importante agregar imágenes a un texto (para ilustrar un concepto, un proceso o un resultado esperado), buscarlas en la bibliografía disponible (`Bibliografia/`) o en internet, priorizando páginas de instituciones de referencia (organismos oficiales, universidades, agencias espaciales, proveedores de datos reconocidos, etc.). Toda imagen debe llevar epígrafe definido y su cita correspondiente en formato APA 7ª edición.

## Con relación a los textos

Convenciones de estilo para los textos del Cuadernillo (nuevos o reescritos):

- Cada texto debe abrir con una introducción que resuma, en pocas líneas, los temas/conceptos que se van a
  abordar en sus distintos apartados — un anticipo del recorrido, no un resumen de las conclusiones.
- Dentro de cada apartado, empezar con una presentación simple del tema o concepto y recién después
  profundizarlo en los párrafos siguientes, llevando al lector de una comprensión básica hacia un nivel
  más avanzado (de grado). No asumir que hay que partir de cero: como se indica arriba, los alumnos ya son
  de 2º año y ya dominan manipulación de datos vectoriales y Procesamiento Digital de Imágenes, así que se
  puede construir sobre ese conocimiento previo en vez de reintroducirlo.
- Cuando ayude a la comprensión, usar ejemplos o metáforas — priorizando los que se conecten con
  herramientas o situaciones de SIG y Teledetección que los alumnos ya conocen.
- Los textos deben estar siempre en **español argentino** (evitar "vosotros", "ordenador" y otros
  regionalismos de otras variantes del español).
- Los textos **no deben ser cortos ni estructurarse a partir de viñetas**: el desarrollo va en prosa
  narrativa. Las listas con viñetas se reservan para situaciones muy puntuales donde una enumeración es
  genuinamente más clara que el texto corrido (por ejemplo, un catálogo de fuentes de datos con sus
  resoluciones) — no como recurso general de organización del texto.

## Contexto curricular (fuente: `Docs/`)

`Docs/` es la fuente de verdad de la planificación — antes de crear o modificar materiales, conviene revisar `Planificacion SIG III 2026.docx` (programa completo) y `Plan_detallado_clases_SIG_III.xlsx` (plan clase por clase) para no desalinearse del cronograma vigente.

- Carga horaria: 60 h totales, 4 h semanales, 15 semanas, segundo cuatrimestre (jueves 14–18 h; consulta martes 14–18 h y aula virtual).
- Programa organizado en **3 unidades**, reflejadas en `Clases/` y `Cuadernillo de catedra/`:
  - **Unidad I** — La estructura de datos ráster (características, fundamentos y potencial del análisis ráster).
  - **Unidad II** — Modelado espacial con ráster (creación de ráster, modelos digitales, modelos de costo, modelo de elevación/superficie, interpolación, combinación, índices, reclasificación).
  - **Unidad III** — Análisis avanzado con ráster (mono y multicriterio, análisis de paisaje, manipulación de ráster / cubos de datos).
- Software de referencia: **QGIS, R o Python**.
- Evaluación: 2 parciales (con recuperatorio) + trabajos prácticos + participación en proceso.
- **Patrón semanal recurrente** (ver `Plan_detallado_clases_SIG_III.xlsx`): tarea pre-clase (lectura del texto del Cuadernillo correspondiente) → presentación en clase (`Clases/`) → tarea post-clase (cuestionario y/o actividad de foro sobre ese texto). Al crear una clase nueva, conviene mantener este mismo patrón de tres pasos y su texto correlativo del Cuadernillo.

## Modelo pedagógico en desarrollo para 2026: teoría asincrónica / práctica en clase

El equipo docente está evaluando, para esta cursada, separar más nítidamente dos instancias dentro de cada tema (todavía **en definición**, no un esquema ya cerrado en `Docs/`):

- **Abordaje conceptual (asincrónico)**: presentación de los conceptos a partir de textos (Cuadernillo) y videos, seguida de actividades de comprobación (cuestionarios, autoevaluaciones) que el alumno resuelve fuera del horario de clase, a su propio ritmo.
- **Actividades prácticas (en clase)**: el tiempo presencial se reserva para la práctica guiada (QGIS/R/Python) sobre datos reales, sin ocupar la clase en exposición teórica.

Esto es una evolución del patrón semanal ya vigente (texto del Cuadernillo → presentación → cuestionario/foro, ver arriba): la idea es reforzar esa separación para que lo conceptual quede resuelto asincrónicamente y la clase se aproveche íntegramente para la práctica. Al ayudar a crear o adaptar materiales, conviene identificar a cuál de las dos instancias corresponde cada pieza y diseñarla en consecuencia: texto/video autocontenido + actividad de comprobación para lo conceptual; consigna con datos y pasos concretos, pensada para resolverse en clase, para lo práctico.

## Aprendizajes de la cursada 2025 a tener en cuenta (`Reflexiones SIG 3 2025.docx`)

Puntos concretos señalados por los docentes, relevantes al diseñar nuevos ejercicios, TPs o parciales:

- En el primer parcial los alumnos tuvieron dificultad manejando **muchas capas a la vez**, sobre todo en el preprocesamiento — vale la pena dar más práctica de ese tipo antes de evaluarla.
- En el segundo parcial, muchos se quedaron en una "zona de confort" con técnicas clásicas (declividad, NDVI vía PDI) y **subutilizaron interpolación, filtros y filtrado** — conviene diseñar consignas que empujen a usar el repertorio completo de la unidad, no solo lo más familiar.
- Las consignas de evaluación deberían ser **más definidas**: listar los procesos esperados y, si aplica, un mínimo de técnicas a usar.
- Dar **más ejercicios por tema** (al menos uno adicional a los ya existentes).
- Incluir algún ejercicio de práctica **más parecido al formato del parcial** (con selección de capas entre varias, como en la evaluación real) para evitar el bloqueo que hubo en el primer parcial.
- Considerar un ejercicio integrador que combine varios temas, a modo de "pre-parcial".
- Mostrar a los alumnos **cómo debería verse el resultado esperado**, no solo la consigna.

## Estructura del repositorio

- `Bibliografia/` — PDFs de referencia (manuales, libros, artículos) y `enlaces_textos.md`, una lista curada de enlaces externos (libro de Víctor Olaya, tutoriales ArcGIS/QGIS, Fragstats, NetCDF, métricas de paisaje) organizada por tema. Agregar lecturas nuevas ahí en vez de crear otro archivo de enlaces — también sirve como primer lugar donde buscar páginas de instituciones de referencia a la hora de conseguir imágenes (ver convención de imágenes en "Rol de Claude" arriba).
- `Clases/` — Material de clase, dividido en tres subcarpetas:
  - `antiguos/` — las 14 presentaciones de cohortes previas (`N_Tema.pptx`, numeradas en el orden de dictado 0–11, alineadas con las Unidades I–III de arriba). Tratarlas como material a revisar, igual que los textos del Cuadernillo.
  - `nuevos/` — presentaciones nuevas en `.qmd` (ver "Producción de textos y presentaciones con Quarto" más abajo); hoy solo la plantilla.
  - `Actividades prácticas/` — parciales, rúbricas y TPs de cohortes previas (`Evaluacion_Parcial_*`, `EvaluacionParcial_II.docx`, `RubicaEvaluacion_Parcial_I.docx`, `Copia de Parcial III.docx`, `TPII.pptx`) más el notebook de Colab `Clase_X_Análisis_espacio_temporal_Cubo_de_Datos.ipynb` sobre cubos de datos geoespaciales — agrupados aparte de las presentaciones teóricas por ser instrumentos de práctica/evaluación.
- `Cuadernillo de catedra/` — El cuadernillo de cátedra, dividido en dos subcarpetas:
  - `antiguos/` — los capítulos `Texto I`–`Texto X` en `.docx`, escritos para **cohortes anteriores**, que acompañan cada clase (ver patrón semanal arriba). **Deben tratarse como material a revisar y actualizar para la cursada actual**, no como texto definitivo — al editarlos, chequear que sigan alineados con la presentación de `Clases/` y con los aprendizajes de la sección anterior. Mantener la convención de nombre `Texto <número romano> - <Título>.docx`.
  - `nuevos/` — textos nuevos/reescritos en `.qmd` (ver "Producción de textos y presentaciones con Quarto" más abajo); hoy Texto I ("Introducción a los Datos Ráster").
- `Docs/` — Documentos de planificación de la asignatura: `Planificacion SIG III 2026.docx` (programa completo), `Plan_detallado_clases_SIG_III.xlsx` (plan clase por clase), `Nota_planif_SIGIII_2026.docx` (nota formal de elevación). Es la fuente de verdad de contenidos mínimos y secuencia de clases.
- Raíz — `Ejercícios_operadores_booleanos_raster.ipynb` (ejercicios de operadores booleanos/monocriterio sobre ráster) y `Figuras_Cuadernillo.ipynb` (genera figuras usadas en los textos del Cuadernillo), más `Reflexiones SIG 3 2025.docx` (ver sección de aprendizajes arriba). También `_quarto.yml`, `references.bib` y `apa.csl` — setup compartido de producción de contenido (ver "Producción de textos y presentaciones con Quarto" más abajo) — y `diagnostico_textos.md`, la revisión tema por tema del Cuadernillo y la planificación.

## Trabajo con los notebooks

Los dos notebooks de la raíz y el de `Clases/` usan `numpy`, `matplotlib`, `scipy` (`convolve2d`) y `rasterio` (instalado dentro del notebook con `!pip install rasterio --quiet`) para armar grillas ráster sintéticas (como arrays enmascarados de `numpy`) y visualizar operaciones ráster (superposición booleana, filtros focales) con fines didácticos — son ilustrativos, no una librería ni un pipeline. `Figuras_Cuadernillo.ipynb` existe específicamente para (re)generar figuras embebidas en los textos del Cuadernillo, así que las figuras regeneradas deben mantenerse visualmente consistentes con cómo se las referencia en esos capítulos. El notebook `Clase_X_...` está escrito para Google Colab (monta Google Drive para acceder a una carpeta de datos compartida), no para ejecución local.

Para ejecutarlos localmente:
```
pip install jupyter numpy matplotlib scipy rasterio
jupyter notebook
```
No hay archivo de requirements, lockfile de dependencias, suite de tests ni CI — instalar los imports que pida cada notebook a medida que aparezcan.

## Producción de textos y presentaciones con Quarto

Desde 2026, los textos nuevos/actualizados del Cuadernillo y las presentaciones nuevas de `Clases/` se
redactan como `.qmd` (Quarto) en vez de `.docx`/`.pptx` directos, y se renderizan al formato final con
`quarto render archivo.qmd`. Piezas del setup, en la raíz del repo:

- **`_quarto.yml`**: proyecto Quarto tipo `default` (sin sitio/book — cada documento se renderiza de forma
  independiente), con `lang: es` y la bibliografía/estilo de cita compartidos.
- **`references.bib`**: bibliografía compartida en BibTeX. Agregar ahí cada fuente nueva que se cite (y
  citarla con `[@clave]` en el texto) en vez de escribir la referencia a mano.
- **`apa.csl`**: estilo de cita APA 7ª edición (bajado del repositorio oficial de estilos CSL), aplica la
  convención de citas de la sección "Rol de Claude" de forma automática: `[@clave]` en el texto se resuelve
  como cita en formato APA 7, y una sección final con `::: {#refs}\n:::` genera la lista de referencias.
- **`date: last-modified`** (en `_quarto.yml`, heredado por todos los `.qmd`): la fecha del documento se
  arma sola a partir de la fecha de modificación del archivo — no hay que actualizarla a mano, se
  refresca cada vez que se guarda el `.qmd` y se vuelve a renderizar.
- **`license:`** (en `_quarto.yml`) con el texto de licencia institucional (CC BY 4.0, SIG III – UNaM):
  ese campo del YAML es solo metadata, **no se renderiza solo** en salidas `docx`/`pdf`. El texto real de
  la licencia vive en `_licencia.md` (raíz del repo, editarlo en ese único archivo, no copiar el texto a
  mano en cada uno) y cada `.qmd` de texto (`docx`/`pdf`) lo suma como **nota al pie**, no como párrafo
  visible. Ojo con la sintaxis: el shortcode `{{< include >}}` **no se resuelve** si va en la misma línea
  que la marca de nota (`[^licencia]: {{< include ... >}}` deja el texto sin expandir, y dentro de
  `author:` en el YAML directamente no se procesa, queda como texto literal `[^licencia]`). Lo que sí
  funciona: colgar la marca de un párrafo del cuerpo (no de un heading, que rompe la compilación LaTeX del
  PDF) y definir la nota en línea aparte, con el include indentado como continuación:

  ```markdown
  *Cátedra SIG III[^licencia]*

  [^licencia]:
      {{< include ../../_licencia.md >}}
  ```

  Las presentaciones `revealjs` son la excepción: ahí la licencia sigue en una slide visible "## Licencia"
  al cierre (ver plantilla), porque una nota al pie no es un patrón aplicable a una diapositiva.
- **`author:`**: todo `.qmd` de texto del Cuadernillo debe declarar el equipo docente en el front matter,
  separado por `;`: `Felipe Sodré Mendes Barros; Demian Lorán; Fabián Rechberger` (sin la nota al pie de
  la licencia, que va colgada aparte del párrafo "Cátedra SIG III", ver punto anterior).
- **Sin comentarios de meta-proceso en el cuerpo**: no dejar notas sobre el estado del borrador, la
  versión o el proceso de edición (tipo "Borrador 2026, versión Quarto (piloto)...") dentro del texto que
  se renderiza. Ese tipo de nota va en el mensaje de commit, en `diagnostico_textos.md`, o como comentario
  HTML `<!-- -->` si tiene que quedar en el archivo sin aparecer en el `.docx`/`.pdf`.
- **Párrafos en una sola línea**: cada párrafo del cuerpo se escribe como una única línea continua en el
  archivo fuente, sin cortes de línea manuales cada ~100 caracteres — el ajuste visual es tarea del editor
  de texto, no del archivo; Markdown no distingue el renderizado final, pero el corte manual complica
  editar y diffear.
- **Nada de "borrador" en el nombre de archivo**: incluso mientras un texto está en desarrollo, el `.qmd`
  (y su `output-file:`) se nombran con la convención de `Texto <número romano> – <Título>` (mismo estilo
  que `antiguos/`, con guion medio "–" y tildes) en vez de un nombre genérico tipo "Texto I - borrador". El
  estado de avance de un texto se sigue en `diagnostico_textos.md` o en el commit, no en el nombre del
  archivo.

**Sobre carpetas `_algo/` (advertencia general, no aplica a `nuevos/`):** Quarto excluye del proyecto
cualquier carpeta que empiece con `_` (es su convención para directorios reservados/de build). Los
borradores vivían antes en carpetas `_borradores/`, que quedaban fuera del escaneo del proyecto y rompían
la herencia de `bibliography:`/`csl:` del `_quarto.yml` — por eso se renombraron a `nuevos/` (sin guion
bajo). Aun así, cada `.qmd` sigue declarando `bibliography:`/`csl:` en su propio encabezado YAML (ruta
relativa hasta la raíz del repo) en vez de depender solo de la herencia del proyecto — es más portable y
evita el problema si en el futuro se crea alguna otra carpeta con `_`. Mantener ese patrón en los `.qmd`
nuevos.

**Nunca correr `quarto render` sin argumentos.** El proyecto barre como "documentos" cualquier `.md`/
`.ipynb` de la raíz del repo (`CLAUDE.md`, `TODO.md`, `diagnostico_textos.md`, los notebooks, etc.), que no
están pensados para renderizarse como Quarto. Siempre apuntar a un archivo puntual:
`quarto render "ruta/al/archivo.qmd"`.

- Texto del Cuadernillo → `format: {docx: default, pdf: default}` en el YAML del `.qmd` (se generan las
  dos salidas: `.docx` para editar/revisar con control de cambios, `.pdf` para distribuir), más
  `output-file: "<nombre>"` explícito para que el `.docx` y el `.pdf` compartan el mismo nombre de archivo
  (si no, Quarto genera el `.pdf` con guiones en vez de espacios). Se trabaja en
  `Cuadernillo de catedra/nuevos/`.
- Presentación de clase → `format: revealjs` en el YAML del `.qmd` (ver plantilla en
  `Clases/nuevos/plantilla-presentacion.qmd`), se trabaja en `Clases/nuevos/`; no reemplaza las `.pptx` de
  `Clases/antiguos/`, es el formato para presentaciones nuevas. No genera PDF por defecto (sería un PDF de
  impresión de slides, un flujo aparte, no simplemente sumar `pdf: default`).
- El `.docx`/`.pptx` de `antiguos/` no se sobreescribe directamente: el `.qmd` y su salida renderizada se
  trabajan en `nuevos/` hasta aprobarse, y recién ahí reemplazan al archivo vigente en `antiguos/`.
- La primera vez que se renderiza a PDF puede fallar/colgarse si TinyTeX necesita instalar un paquete de
  LaTeX (p. ej. `hyphen-spanish` por `lang: es`) y su repositorio configurado no responde — en este
  entorno pasó con el mirror por defecto; se resolvió apuntando `tlmgr` a un mirror de CTAN que sí
  respondía. Si vuelve a pasar, no es un problema del `.qmd`.

## Convenciones a mantener

- `antiguos/` vs. `nuevos/` (y, en `Clases/`, `Actividades prácticas/` aparte): mantener esta separación
  al agregar material — cohortes previas en `antiguos/`, lo que se está creando/revisando ahora en
  `nuevos/`, instrumentos de práctica/evaluación de `Clases/` en `Actividades prácticas/`. No usar nombres
  de carpeta con `_` inicial para contenido nuevo (ver advertencia de Quarto arriba).
- La numeración de clases en `Clases/antiguos/` y la numeración romana de capítulos en `Cuadernillo de catedra/antiguos/` están alineadas intencionalmente por tema — al editar una, revisar si la presentación/capítulo correlativo necesita una actualización equivalente.
- Los nombres de archivo mezclan caracteres acentuados en español y espacios; mantener ese mismo estilo al agregar archivos nuevos (no normalizar/renombrar archivos existentes como efecto secundario de una edición no relacionada).
