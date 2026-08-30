"""Estética retro (arcade de los 80/90, pixel-art) para la interfaz del juego.

`CSS_RETRO` se inyecta una sola vez desde `app.py` con `st.markdown(CSS_RETRO,
unsafe_allow_html=True)`. No toca `graficos_raster.py`: las grillas de las capas se siguen dibujando
con `plot_raster` sin modificar, pasándole nada más que una paleta de colores (`CMAP_CAPAS`,
`CMAP_RESULTADO`) que combina bien con el resto de la pantalla — la propia grilla de celdas grandes ya
tiene, por su naturaleza, una lectura "pixel art".
"""

TITULO_JUEGO = "ÁLGEBRA DE MAPAS: EL DESAFÍO"
AUTORIA = "Felipe Sodré Mendes Barros"
AMBITO = (
    "Tecnicatura Universitaria en Sistemas de Información Geográfica y Teledetección — "
    "Facultad de Ciencias Forestales — Universidad Nacional de Misiones (UNaM), Argentina"
)

# Paletas para plot_raster: oscuras y de alto contraste, en línea con el resto de la piel retro.
CMAP_CAPAS = "viridis"
CMAP_RESULTADO = "plasma"
CMAP_BOOLEANO = "spring"

CSS_RETRO = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

:root {
    --retro-fondo: #0d0221;
    --retro-panel: #1a0b3d;
    --retro-borde: #f7ff00;
    --retro-acento: #00f5d4;
    --retro-peligro: #ff2079;
    --retro-texto: #f4f4f4;
}

html, body, [class*="css"] {
    font-family: 'Press Start 2P', monospace !important;
}

.stApp {
    background: var(--retro-fondo);
    color: var(--retro-texto);
}

h1, h2, h3 {
    color: var(--retro-borde) !important;
    text-shadow: 3px 3px 0 var(--retro-peligro);
    letter-spacing: 1px;
}

/* Streamlit no expone nombres de clase estables: usa siempre `data-testid`, que sí lo son. */
button[data-testid^="stBaseButton-secondary"],
button[data-testid^="stBaseButton-primary"] {
    font-family: 'Press Start 2P', monospace !important;
    background: var(--retro-panel) !important;
    color: var(--retro-acento) !important;
    border: 3px solid var(--retro-borde) !important;
    border-radius: 0 !important;
    box-shadow: 4px 4px 0 var(--retro-peligro);
    padding: 0.6em 1em !important;
}

button[data-testid^="stBaseButton-secondary"]:hover,
button[data-testid^="stBaseButton-primary"]:hover {
    color: var(--retro-fondo) !important;
    background: var(--retro-acento) !important;
    border-color: var(--retro-acento) !important;
}

button[data-testid^="stBaseButton-secondary"] p,
button[data-testid^="stBaseButton-primary"] p {
    font-family: 'Press Start 2P', monospace !important;
    color: inherit !important;
}

input[data-testid="stTextInputField"] {
    font-family: 'Press Start 2P', monospace !important;
    background: var(--retro-panel) !important;
    color: var(--retro-texto) !important;
    border: 3px solid var(--retro-borde) !important;
    border-radius: 0 !important;
}

.retro-panel {
    background: var(--retro-panel);
    border: 3px solid var(--retro-borde);
    padding: 1em;
    margin-bottom: 1em;
    box-shadow: 6px 6px 0 rgba(0, 0, 0, 0.4);
}

.retro-vidas {
    color: var(--retro-peligro);
    font-size: 1.4em;
    letter-spacing: 4px;
}

.retro-credito {
    color: var(--retro-acento);
    font-size: 0.6em;
    line-height: 1.8;
    text-align: center;
}

div[data-testid="stRadio"] label[data-testid="stWidgetLabel"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"] p {
    font-family: 'Press Start 2P', monospace !important;
    color: var(--retro-texto) !important;
    font-size: 0.85em;
}

.retro-tabla th, .retro-tabla td {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 0.7em;
    padding: 0.5em;
    border: 2px solid var(--retro-borde);
}
</style>
"""
