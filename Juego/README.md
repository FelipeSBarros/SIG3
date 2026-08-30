# Álgebra de mapas: el desafío

Juego de práctica en Streamlit para interpretar álgebra de mapas: identificar qué operación se aplicó
entre capas ráster a partir del resultado, o adivinar el resultado correcto a partir de las capas y la
operación. Preguntas generadas proceduralmente, con dificultad creciente (5 niveles, alineados al orden
del Cuadernillo: aritmética local, constante/ponderación, condicionales, compuestos booleanos y
funciones estadísticas, e integrador con Sin Dato). 3 vidas, ranking de los 5 mejores puntajes.

**Autoría**: Felipe Sodré Mendes Barros — Tecnicatura Universitaria en Sistemas de Información Geográfica
y Teledetección, Facultad de Ciencias Forestales, Universidad Nacional de Misiones (UNaM), Argentina.

## Correr localmente

Desde la raíz del repositorio (no desde `Juego/`, porque `app.py` necesita encontrar `_quarto.yml` para
ubicar `graficos_raster.py`):

```
pip install -r Juego/requirements.txt
streamlit run Juego/app.py
```

## Desplegar en Streamlit Community Cloud

Apuntar el "Main file path" a `Juego/app.py`; Streamlit Cloud toma `Juego/requirements.txt` porque está
en la misma carpeta que el archivo principal.

**Advertencia sobre el ranking**: `Juego/ranking.db` (SQLite) persiste mientras la app siga activa
(incluso si se "duerme" por inactividad y se despierta), pero **se reinicia en cada redeploy** (cada vez
que se hace push de un cambio nuevo al repositorio conectado). Es aceptable para un juego de práctica,
no para llevar un registro oficial — si en el futuro hace falta que el ranking sobreviva a los redeploys,
hay que migrar `Juego/ranking.py` a un backend externo (por ejemplo, Google Sheets o una base remota).

## Estructura

- `app.py` — entrypoint de Streamlit (pantallas, `st.session_state`).
- `preguntas.py` — generadores procedurales de preguntas por nivel de dificultad.
- `ranking.py` — persistencia del ranking en SQLite.
- `estilo.py` — CSS de la estética retro (pixel-art, arcade de los 80/90) y paletas de color para
  `plot_raster` (definido en `graficos_raster.py`, raíz del repo — no se duplica ni se modifica acá).
