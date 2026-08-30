"""Juego de práctica de álgebra de mapas — entrypoint de Streamlit.

Correr localmente desde la raíz del repo con:
    streamlit run Juego/app.py

Ver `Juego/README.md` para el despliegue en Streamlit Community Cloud y la advertencia sobre la
persistencia del ranking.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import streamlit as st

# --- Ubicar la raíz del repo para importar graficos_raster.py sin duplicarlo ---
# Mismo patrón que usa Clases/Actividades prácticas/Figuras_Cuadernillo.ipynb.


def _find_repo_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "_quarto.yml").exists():
            return parent
    raise FileNotFoundError("No se encontró la raíz del repositorio (_quarto.yml)")


REPO_ROOT = _find_repo_root(Path(__file__).resolve().parent)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from graficos_raster import plot_raster  # noqa: E402

import estilo  # noqa: E402
import ranking  # noqa: E402
from preguntas import generar_pregunta  # noqa: E402

VIDAS_INICIALES = 3
RACHA_PARA_SUBIR_NIVEL = 3
NIVEL_MAXIMO = 5


# --- Configuración de página y estilo ---

st.set_page_config(page_title=estilo.TITULO_JUEGO, page_icon="👾", layout="centered")
st.markdown(estilo.CSS_RETRO, unsafe_allow_html=True)
ranking.init_db()


# --- Estado del juego ---

def _estado_inicial() -> None:
    st.session_state.nombre = None
    st.session_state.intento_id = None
    st.session_state.vidas = VIDAS_INICIALES
    st.session_state.puntaje = 0
    st.session_state.nivel = 1
    st.session_state.racha = 0
    st.session_state.pregunta_actual = None
    st.session_state.modo_actual = None
    st.session_state.terminado = False
    st.session_state.retroalimentacion = None


if "nombre" not in st.session_state:
    _estado_inicial()


def _reiniciar_juego() -> None:
    _estado_inicial()


def _asegurar_pregunta() -> None:
    if st.session_state.pregunta_actual is None:
        rng = np.random.default_rng()
        st.session_state.pregunta_actual = generar_pregunta(st.session_state.nivel, rng)
        st.session_state.modo_actual = rng.choice(["operacion", "resultado"])
        # Ojo: `retroalimentacion` no se borra acá. Cuando se genera la pregunta siguiente después de
        # responder, todavía queremos mostrar en esta misma pasada el resultado de la respuesta
        # anterior (_responder ya la dejó en el valor correcto); recién la próxima respuesta la
        # pisa con su propio mensaje.


def _terminar_partida() -> None:
    ranking.actualizar_puntaje(st.session_state.intento_id, st.session_state.puntaje, st.session_state.nivel)
    st.session_state.terminado = True


def _responder(correcto: bool) -> None:
    if correcto:
        st.session_state.puntaje += 1
        st.session_state.racha += 1
        st.session_state.retroalimentacion = ("ok", "¡Correcto!")
        if st.session_state.racha >= RACHA_PARA_SUBIR_NIVEL and st.session_state.nivel < NIVEL_MAXIMO:
            st.session_state.nivel += 1
            st.session_state.racha = 0
            st.session_state.retroalimentacion = ("ok", f"¡Correcto! Subiste al nivel {st.session_state.nivel}.")
    else:
        st.session_state.vidas -= 1
        st.session_state.racha = 0
        st.session_state.retroalimentacion = ("mal", "Incorrecto, perdiste una vida.")
    st.session_state.pregunta_actual = None
    if st.session_state.vidas <= 0:
        _terminar_partida()


# --- Utilidades de dibujo ---

def _dibujar_grilla(nombre: str, arr: np.ndarray, categorical: bool, cmap: str, vmin: float, vmax: float):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(2.6, 2.6))
    fig.patch.set_facecolor("#1a0b3d")
    plot_raster(ax, arr, title=nombre, categorical=categorical, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.title.set_color("#f4f4f4")
    return fig


def _mostrar_capas(pregunta) -> None:
    cmap = estilo.CMAP_BOOLEANO if pregunta.categorical_capas else estilo.CMAP_CAPAS
    # Cada capa de entrada se escala a su propio rango (salvo que sea booleana), para que se lea bien
    # por separado en vez de aplanarse contra la escala del resultado.
    vmin, vmax = (0, 1) if pregunta.categorical_capas else (None, None)
    columnas = st.columns(len(pregunta.capas))
    for columna, (nombre, arr) in zip(columnas, pregunta.capas):
        with columna:
            fig = _dibujar_grilla(nombre, arr, pregunta.categorical_capas, cmap, vmin, vmax)
            st.pyplot(fig, clear_figure=True)


def _mostrar_grilla_unica(titulo: str, arr: np.ndarray, pregunta) -> None:
    cmap = estilo.CMAP_BOOLEANO if pregunta.categorical_resultado else estilo.CMAP_RESULTADO
    fig = _dibujar_grilla(
        titulo, arr, pregunta.categorical_resultado, cmap, pregunta.vmin_resultado, pregunta.vmax_resultado
    )
    st.pyplot(fig, clear_figure=True)


# --- Pantallas ---

def _pantalla_titulo() -> None:
    st.markdown(f"<h1 style='text-align:center'>{estilo.TITULO_JUEGO}</h1>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='retro-credito'>Autoría: {estilo.AUTORIA}<br>{estilo.AMBITO}</div>",
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<div class='retro-panel'>Interpretá el álgebra de mapas: identificá qué operación se aplicó "
        "entre capas ráster, o adiviná el resultado correcto. Tenés 3 vidas — ¡suerte!</div>",
        unsafe_allow_html=True,
    )
    with st.form("form_nombre"):
        nombre = st.text_input("Ingresá tu nombre para jugar")
        enviado = st.form_submit_button("JUGAR")
    if enviado and nombre.strip():
        st.session_state.nombre = nombre.strip()
        st.session_state.intento_id = ranking.registrar_inicio(st.session_state.nombre)
        st.rerun()
    elif enviado:
        st.warning("Ingresá un nombre antes de jugar.")


def _pantalla_juego() -> None:
    _asegurar_pregunta()
    pregunta = st.session_state.pregunta_actual
    modo = st.session_state.modo_actual

    vidas = "♥ " * st.session_state.vidas
    st.markdown(
        f"<div class='retro-panel'>"
        f"<span class='retro-vidas'>{vidas}</span><br>"
        f"NIVEL {st.session_state.nivel}/{NIVEL_MAXIMO} &nbsp;|&nbsp; PUNTAJE: {st.session_state.puntaje}"
        f"</div>",
        unsafe_allow_html=True,
    )

    if st.session_state.retroalimentacion:
        tipo, mensaje = st.session_state.retroalimentacion
        (st.success if tipo == "ok" else st.error)(mensaje)

    if modo == "operacion":
        st.subheader("¿Qué operación se aplicó?")
        _mostrar_capas(pregunta)
        _, columna_resultado, _ = st.columns([1, 2, 1])
        with columna_resultado:
            _mostrar_grilla_unica("Resultado", pregunta.resultado, pregunta)
        with st.form("form_operacion"):
            elegida = st.radio("Elegí la operación:", pregunta.opciones_operacion, index=None)
            enviado = st.form_submit_button("CONFIRMAR")
        if enviado:
            if elegida is None:
                st.warning("Elegí una opción antes de confirmar.")
            else:
                _responder(elegida == pregunta.respuesta_operacion)
                st.rerun()
    else:
        st.subheader("¿Cuál es el resultado?")
        _mostrar_capas(pregunta)
        st.markdown(
            f"<div class='retro-panel'>Operación: {pregunta.operacion_formula}</div>",
            unsafe_allow_html=True,
        )
        columnas = st.columns(len(pregunta.opciones_resultado))
        etiquetas = "ABCD"
        for i, (columna, candidato) in enumerate(zip(columnas, pregunta.opciones_resultado)):
            with columna:
                _mostrar_grilla_unica(f"Opción {etiquetas[i]}", candidato, pregunta)
                if st.button(f"ELEGIR {etiquetas[i]}", key=f"elegir_resultado_{i}"):
                    _responder(i == pregunta.indice_respuesta_resultado)
                    st.rerun()


def _pantalla_fin() -> None:
    st.markdown(f"<h1 style='text-align:center'>FIN DEL JUEGO</h1>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='retro-panel' style='text-align:center'>"
        f"{st.session_state.nombre}, terminaste con <b>{st.session_state.puntaje}</b> puntos "
        f"(nivel {st.session_state.nivel}/{NIVEL_MAXIMO})."
        f"</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<h3>TOP 5</h3>", unsafe_allow_html=True)
    filas = ranking.top_5()
    if filas:
        html = "<table class='retro-tabla' style='width:100%; border-collapse:collapse'>"
        html += "<tr><th>Nombre</th><th>Puntaje</th><th>Nivel</th><th>Fecha y hora</th></tr>"
        for fila in filas:
            html += (
                f"<tr><td>{fila['nombre']}</td><td>{fila['puntaje']}</td>"
                f"<td>{fila['nivel_alcanzado']}</td><td>{fila['iniciado_en']}</td></tr>"
            )
        html += "</table>"
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.info("Todavía no hay puntajes registrados.")

    if st.button("JUGAR DE NUEVO"):
        _reiniciar_juego()
        st.rerun()


# --- Enrutamiento ---

if st.session_state.nombre is None:
    _pantalla_titulo()
elif st.session_state.terminado:
    _pantalla_fin()
else:
    _pantalla_juego()
