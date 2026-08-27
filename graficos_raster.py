"""Utilidades de graficado para ilustrar operaciones de álgebra de mapas con rásters sintéticos.

Pensado para generar las figuras didácticas del Cuadernillo de cátedra (ver
`Clases/Actividades prácticas/Figuras_Cuadernillo.ipynb`) y, más adelante, para reutilizarse en el
juego/quiz de operadores lógicos que se construya en Streamlit: `plot_raster` dibuja un único panel
(un ráster, con el valor de cada celda escrito encima) y está pensada para combinarse en figuras de
varios paneles con `plt.subplots`, o para insertarse directamente en una pantalla de Streamlit.

Sin dependencias más allá de numpy y matplotlib, ya usadas en el resto de los notebooks del repositorio.
"""

from __future__ import annotations

import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, Normalize
from matplotlib.patches import Rectangle


def plot_raster(
    ax,
    data,
    title=None,
    cmap="Greys",
    vmin=None,
    vmax=None,
    categorical=False,
    text_color="auto",
    fontsize=12,
    fontweight="bold",
    valfmt="{:g}",
    nodata_color="0.85",
    nodata_label="SD",
    nodata_border_color="red",
    nodata_border_width=1.5,
    highlight=None,
    highlight_style="dashed",
    highlight_color="red",
):
    """Dibuja un ráster en `ax`: una grilla de celdas con su valor numérico escrito encima.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Panel donde dibujar (por ejemplo, uno de los ejes devueltos por `plt.subplots`).
    data : array_like o numpy.ma.MaskedArray
        Grilla 2D de valores. Las celdas enmascaradas (`numpy.ma`) representan NoData: se dibujan
        con relleno gris, la etiqueta `nodata_label` en vez de un valor, y un borde de color propio
        (`nodata_border_color`), para que salten a la vista aunque el resto del panel use un
        colormap donde el gris de NoData pase desapercibido.
    title : str, opcional
        Título del panel.
    cmap : str
        Colormap para las celdas con datos.
    vmin, vmax : float, opcional
        Límites de la escala de color. Conviene fijarlos cuando se comparan varios paneles entre sí
        (por ejemplo, capas de entrada y su resultado), para que el color sea comparable.
    categorical : bool
        Si es `True`, trata los valores enteros de `vmin` a `vmax` como clases discretas: cada
        entero recibe un color propio y bien diferenciado (vía `BoundaryNorm`) en lugar de un
        degradé continuo. Conviene activarlo para capas categóricas, sobre todo cuando las clases
        son nominales y no tienen un orden natural (por ejemplo, tipos de uso del suelo) — ahí
        además conviene pasar un `cmap` cualitativo (`"Set2"`, `"tab10"`, etc.) en vez de uno
        secuencial, para no sugerir un orden que no existe. Para categorías ordinales (por ejemplo,
        una pendiente clasificada en baja/media/alta) también puede activarse, manteniendo un `cmap`
        secuencial para conservar la noción de orden.
    text_color : "auto" o color de matplotlib
        Por defecto ("auto") el texto de cada celda se pinta blanco o negro según el brillo del
        color de fondo de esa celda, para que siga siendo legible incluso en colormaps donde los
        valores altos quedan casi negros (por ejemplo "Greys"). Pasar un color fijo desactiva ese
        cálculo automático.
    fontsize, fontweight : estilo del texto de cada celda.
    valfmt : str
        Formato de cada valor (por defecto, `{:g}` para no arrastrar decimales innecesarios).
    nodata_color : color de relleno de las celdas NoData.
    nodata_label : str o None
        Texto que se escribe sobre cada celda NoData (por defecto, `"SD"` de "sin dato"). `None`
        para no escribir nada.
    nodata_border_color : color o None
        Color del borde que remarca cada celda NoData. `None` para no dibujar borde. Se usa un trazo
        más fino que `highlight` (ver abajo) para no confundir ambos recursos si coinciden en una
        misma celda: el borde de NoData señala "acá falta el dato", el resaltado de `highlight`
        señala "seguí esta celda en particular".
    nodata_border_width : float
        Grosor del borde de NoData.
    highlight : list[tuple[int, int]], opcional
        Lista de celdas `(fila, columna)` a resaltar con un recuadro, para que el alumnado pueda
        seguir una celda puntual entre distintos paneles de una misma figura.
    highlight_style : "dashed" o "solid"
        Estilo del recuadro de resaltado.
    highlight_color : color del recuadro de resaltado.
    """
    arr = ma.masked_invalid(data) if not ma.isMaskedArray(data) else ma.asarray(data)
    rows, cols = arr.shape

    vmin_eff = vmin if vmin is not None else arr.min()
    vmax_eff = vmax if vmax is not None else arr.max()

    if categorical:
        n_clases = int(round(vmax_eff - vmin_eff)) + 1
        cmap_obj = plt.get_cmap(cmap, n_clases)
        norm = BoundaryNorm(np.arange(vmin_eff - 0.5, vmax_eff + 1.5, 1), n_clases)
    else:
        cmap_obj = plt.get_cmap(cmap)
        norm = Normalize(vmin=vmin_eff, vmax=vmax_eff)
    cmap_obj = cmap_obj.copy()
    cmap_obj.set_bad(nodata_color)

    ax.imshow(arr, cmap=cmap_obj, norm=norm, origin="upper")

    for i in range(rows):
        for j in range(cols):
            if ma.is_masked(arr[i, j]):
                if nodata_border_color:
                    ax.add_patch(
                        Rectangle(
                            (j - 0.5, i - 0.5),
                            1,
                            1,
                            fill=False,
                            edgecolor=nodata_border_color,
                            linewidth=nodata_border_width,
                        )
                    )
                if nodata_label:
                    ax.text(
                        j,
                        i,
                        nodata_label,
                        color="black",
                        ha="center",
                        va="center",
                        fontweight=fontweight,
                        fontsize=fontsize,
                    )
                continue
            value = arr[i, j]
            if text_color == "auto":
                r, g, b, _ = cmap_obj(norm(value))
                luminancia = 0.299 * r + 0.587 * g + 0.114 * b
                color = "white" if luminancia < 0.5 else "black"
            else:
                color = text_color
            ax.text(
                j,
                i,
                valfmt.format(value),
                color=color,
                ha="center",
                va="center",
                fontweight=fontweight,
                fontsize=fontsize,
            )

    for i, j in highlight or []:
        ax.add_patch(
            Rectangle(
                (j - 0.5, i - 0.5),
                1,
                1,
                fill=False,
                edgecolor=highlight_color,
                linewidth=2.5,
                linestyle="dashed" if highlight_style == "dashed" else "solid",
            )
        )

    if title:
        ax.set_title(title, fontsize=fontsize + 2, fontweight="bold")

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
        spine.set_linewidth(1)
