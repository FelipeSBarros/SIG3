"""Generadores procedurales de preguntas para el juego de álgebra de mapas.

Cada `generar_nivel_N(rng)` arma una `Pregunta`: una o más capas ráster sintéticas (títulos genéricos,
sin nombrar la operación, mismo criterio que las preguntas de "operación misteriosa" de
`Cuestionarios/nuevos/Texto III – Álgebra de mapas.gift`), el resultado real de aplicarles una operación,
y los datos necesarios para presentarla en cualquiera de los dos modos del juego:

- "Indicá la operación realizada": se listan los nombres de operación en `opciones_operacion`
  (`respuesta_operacion` es la correcta).
- "Indicá el resultado": se listan grillas candidatas en `opciones_resultado`
  (`indice_respuesta_resultado` marca cuál es la correcta).

Cada generador verifica que los distractores nunca coincidan entre sí ni con la respuesta correcta
(si coinciden, se vuelve a intentar con nuevos valores al azar) para que ninguna pregunta quede
ambigua. En particular, el nivel 4 evita a propósito ofrecer a la vez "AND" y "min()" (o "OR" y "max()")
como opciones separadas, porque sobre capas booleanas dan siempre el mismo resultado — la equivalencia
que explica Texto V, no un distractor válido.

Las capas de entrada y las grillas de resultado/candidatos llevan escalas de color separadas
(`categorical_capas`/`categorical_resultado`, `vmin_resultado`/`vmax_resultado`): cada capa de entrada
se deja escalar a su propio rango (salvo que sea booleana) para que se lea bien por separado, mientras
que el resultado y sus distractores comparten una única escala entre sí, para que sean comparables.
"""

from __future__ import annotations

import operator
from dataclasses import dataclass

import numpy as np

MAX_INTENTOS = 30


@dataclass
class Pregunta:
    nivel: int
    capas: list[tuple[str, np.ndarray]]
    operacion_nombre: str
    operacion_formula: str
    resultado: np.ndarray
    opciones_operacion: list[str]
    respuesta_operacion: str
    opciones_resultado: list[np.ndarray]
    indice_respuesta_resultado: int
    vmin_resultado: float
    vmax_resultado: float
    categorical_capas: bool = False
    categorical_resultado: bool = False
    nodata: bool = False


def _distintos(*arrays: np.ndarray) -> bool:
    """True si todas las grillas son distintas entre sí (celda a celda)."""
    for i in range(len(arrays)):
        for j in range(i + 1, len(arrays)):
            a, b = arrays[i], arrays[j]
            if a.shape != b.shape:
                continue
            with np.errstate(invalid="ignore"):
                iguales = np.array_equal(a, b, equal_nan=True)
            if iguales:
                return False
    return True


def _shuffle(rng: np.random.Generator, opciones: list) -> list:
    """Baraja una lista de opciones de texto (ya incluye a la correcta)."""
    orden = rng.permutation(len(opciones))
    return [opciones[i] for i in orden]


def _shuffle_resultados(rng: np.random.Generator, correcto: np.ndarray, distractores: list[np.ndarray]):
    candidatos = [correcto, *distractores]
    orden = list(rng.permutation(len(candidatos)))
    barajados = [candidatos[i] for i in orden]
    indice_correcto = orden.index(0)
    return barajados, indice_correcto


# ---------------------------------------------------------------------------
# Nivel 1 — Aritmética local simple (Texto III)
# ---------------------------------------------------------------------------

_OPS_NIVEL_1 = {
    "Suma": (operator.add, '"Capa A" + "Capa B"'),
    "Resta": (operator.sub, '"Capa A" − "Capa B"'),
    "Multiplicación": (operator.mul, '"Capa A" × "Capa B"'),
}


def generar_nivel_1(rng: np.random.Generator) -> Pregunta:
    for _ in range(MAX_INTENTOS):
        capa_a = rng.integers(1, 10, size=(3, 3))
        capa_b = rng.integers(1, 10, size=(3, 3))
        nombre_correcta = rng.choice(list(_OPS_NIVEL_1))
        resultados = {nombre: fn(capa_a, capa_b) for nombre, (fn, _formula) in _OPS_NIVEL_1.items()}
        if not _distintos(*resultados.values()):
            continue
        resultado = resultados[nombre_correcta]
        opciones_op = _shuffle(rng, list(_OPS_NIVEL_1))
        distractores = [v for k, v in resultados.items() if k != nombre_correcta]
        opciones_res, indice_res = _shuffle_resultados(rng, resultado, distractores)
        return Pregunta(
            nivel=1,
            capas=[("Capa A", capa_a), ("Capa B", capa_b)],
            operacion_nombre=nombre_correcta,
            operacion_formula=_OPS_NIVEL_1[nombre_correcta][1],
            resultado=resultado,
            opciones_operacion=opciones_op,
            respuesta_operacion=nombre_correcta,
            opciones_resultado=opciones_res,
            indice_respuesta_resultado=indice_res,
            vmin_resultado=min(a.min() for a in resultados.values()),
            vmax_resultado=max(a.max() for a in resultados.values()),
        )
    raise RuntimeError("No se pudo generar una pregunta de nivel 1 sin distractores duplicados")


# ---------------------------------------------------------------------------
# Nivel 2 — Constante y ponderación (Texto III: jerarquización y trazabilidad)
# ---------------------------------------------------------------------------

def _nivel_2_constante(rng: np.random.Generator) -> Pregunta | None:
    capa_a = rng.integers(1, 10, size=(3, 3))
    constante = int(rng.integers(2, 6))
    capa_b = np.full((3, 3), constante)
    ops = {
        "Multiplicación por una constante": (capa_a * capa_b, '"Capa A" × "Capa B"'),
        "Suma": (capa_a + capa_b, '"Capa A" + "Capa B"'),
        "Resta": (capa_a - capa_b, '"Capa A" − "Capa B"'),
    }
    resultados = {k: v[0] for k, v in ops.items()}
    if not _distintos(*resultados.values()):
        return None
    nombre_correcta = "Multiplicación por una constante"
    resultado = resultados[nombre_correcta]
    opciones_op = _shuffle(rng, list(ops))
    distractores = [v for k, v in resultados.items() if k != nombre_correcta]
    opciones_res, indice_res = _shuffle_resultados(rng, resultado, distractores)
    return Pregunta(
        nivel=2,
        capas=[("Capa A", capa_a), ("Capa B (uniforme)", capa_b)],
        operacion_nombre=nombre_correcta,
        operacion_formula=ops[nombre_correcta][1],
        resultado=resultado,
        opciones_operacion=opciones_op,
        respuesta_operacion=nombre_correcta,
        opciones_resultado=opciones_res,
        indice_respuesta_resultado=indice_res,
        vmin_resultado=min(a.min() for a in resultados.values()),
        vmax_resultado=max(a.max() for a in resultados.values()),
    )


def _nivel_2_trazabilidad(rng: np.random.Generator) -> Pregunta | None:
    pendiente = rng.integers(0, 3, size=(3, 3))
    uso_suelo = rng.integers(1, 5, size=(3, 3))
    ops = {
        "Suma ponderada (trazable): pendiente × 10 + uso de suelo": (
            pendiente * 10 + uso_suelo,
            '"Pendiente" × 10 + "Uso de suelo"',
        ),
        "Suma simple (ambigua): pendiente + uso de suelo": (
            pendiente + uso_suelo,
            '"Pendiente" + "Uso de suelo"',
        ),
    }
    resultados = {k: v[0] for k, v in ops.items()}
    if not _distintos(*resultados.values()):
        return None
    nombre_correcta = "Suma ponderada (trazable): pendiente × 10 + uso de suelo"
    resultado = resultados[nombre_correcta]
    opciones_op = _shuffle(rng, list(ops))
    distractores = [v for k, v in resultados.items() if k != nombre_correcta]
    opciones_res, indice_res = _shuffle_resultados(rng, resultado, distractores)
    return Pregunta(
        nivel=2,
        capas=[("Pendiente (0-2)", pendiente), ("Uso de suelo (1-4)", uso_suelo)],
        operacion_nombre=nombre_correcta,
        operacion_formula=ops[nombre_correcta][1],
        resultado=resultado,
        opciones_operacion=opciones_op,
        respuesta_operacion=nombre_correcta,
        opciones_resultado=opciones_res,
        indice_respuesta_resultado=indice_res,
        vmin_resultado=min(a.min() for a in resultados.values()),
        vmax_resultado=max(a.max() for a in resultados.values()),
    )


def generar_nivel_2(rng: np.random.Generator) -> Pregunta:
    variante = _nivel_2_constante if rng.random() < 0.5 else _nivel_2_trazabilidad
    for _ in range(MAX_INTENTOS):
        pregunta = variante(rng)
        if pregunta is not None:
            return pregunta
    raise RuntimeError("No se pudo generar una pregunta de nivel 2 sin distractores duplicados")


# ---------------------------------------------------------------------------
# Nivel 3 — Condicionales / comparadores (Texto V)
# ---------------------------------------------------------------------------

_COMPARADORES = {
    "=": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
}


def generar_nivel_3(rng: np.random.Generator) -> Pregunta:
    for _ in range(MAX_INTENTOS):
        capa = rng.integers(1, 31, size=(3, 3))
        umbral = int(rng.integers(5, 26))
        simbolo_correcto = rng.choice(list(_COMPARADORES))
        resultado = _COMPARADORES[simbolo_correcto](capa, umbral).astype(int)
        if resultado.sum() in (0, resultado.size):
            continue  # máscara toda en 0 o toda en 1: poco informativa para el juego

        candidatos_simbolo = [s for s in _COMPARADORES if s != simbolo_correcto]
        rng.shuffle(candidatos_simbolo)
        distractores_simbolo = []
        distractores_resultado = []
        for simbolo in candidatos_simbolo:
            mascara = _COMPARADORES[simbolo](capa, umbral).astype(int)
            if _distintos(resultado, mascara, *distractores_resultado):
                distractores_simbolo.append(simbolo)
                distractores_resultado.append(mascara)
            if len(distractores_simbolo) == 2:
                break
        if len(distractores_simbolo) < 2:
            continue

        nombre_correcta = f'"Capa" {simbolo_correcto} {umbral}'
        opciones_nombre = [nombre_correcta] + [f'"Capa" {s} {umbral}' for s in distractores_simbolo]
        opciones_op = _shuffle(rng, opciones_nombre)
        opciones_res, indice_res = _shuffle_resultados(rng, resultado, distractores_resultado)
        return Pregunta(
            nivel=3,
            capas=[("Capa", capa)],
            operacion_nombre=nombre_correcta,
            operacion_formula=nombre_correcta,
            resultado=resultado,
            opciones_operacion=opciones_op,
            respuesta_operacion=nombre_correcta,
            opciones_resultado=opciones_res,
            indice_respuesta_resultado=indice_res,
            vmin_resultado=0,
            vmax_resultado=1,
            categorical_resultado=True,
        )
    raise RuntimeError("No se pudo generar una pregunta de nivel 3 sin distractores duplicados")


# ---------------------------------------------------------------------------
# Nivel 4 — Compuestos booleanos y funciones estadísticas (Texto V)
# ---------------------------------------------------------------------------

def generar_nivel_4(rng: np.random.Generator) -> Pregunta:
    for _ in range(MAX_INTENTOS):
        capa_a = rng.integers(0, 2, size=(3, 3))
        capa_b = rng.integers(0, 2, size=(3, 3))
        capa_c = rng.integers(0, 2, size=(3, 3))
        ops = {
            "AND (intersección: min entre las tres capas)": (
                np.minimum(np.minimum(capa_a, capa_b), capa_c),
                'min("Capa A", "Capa B", "Capa C")',
            ),
            "OR (unión: max entre las tres capas)": (
                np.maximum(np.maximum(capa_a, capa_b), capa_c),
                'max("Capa A", "Capa B", "Capa C")',
            ),
            "sum() (acumulado entre las tres capas)": (
                capa_a + capa_b + capa_c,
                'sum("Capa A", "Capa B", "Capa C")',
            ),
        }
        resultados = {k: v[0] for k, v in ops.items()}
        if not _distintos(*resultados.values()):
            continue
        nombre_correcta = rng.choice(list(ops))
        resultado = resultados[nombre_correcta]
        opciones_op = _shuffle(rng, list(ops))
        distractores = [v for k, v in resultados.items() if k != nombre_correcta]
        opciones_res, indice_res = _shuffle_resultados(rng, resultado, distractores)
        return Pregunta(
            nivel=4,
            capas=[("Capa A", capa_a), ("Capa B", capa_b), ("Capa C", capa_c)],
            operacion_nombre=nombre_correcta,
            operacion_formula=ops[nombre_correcta][1],
            resultado=resultado,
            opciones_operacion=opciones_op,
            respuesta_operacion=nombre_correcta,
            opciones_resultado=opciones_res,
            indice_respuesta_resultado=indice_res,
            vmin_resultado=0,
            vmax_resultado=max(a.max() for a in resultados.values()),
            categorical_capas=True,
            categorical_resultado=True,
        )
    raise RuntimeError("No se pudo generar una pregunta de nivel 4 sin distractores duplicados")


# ---------------------------------------------------------------------------
# Nivel 5 — Integrador: máscara + capa, o combinación con Sin Dato (Texto III/V)
# ---------------------------------------------------------------------------

def _nivel_5_mascara(rng: np.random.Generator) -> Pregunta | None:
    pendiente = rng.integers(1, 31, size=(4, 4))
    capa_extra = rng.integers(1, 10, size=(4, 4))
    umbral = int(rng.integers(10, 21))
    mascara = (pendiente >= umbral).astype(int)

    ops = {
        f'("Pendiente" >= {umbral}) × "Capa extra"': (mascara * capa_extra, "máscara correctamente aplicada"),
        '"Capa extra" (sin aplicar la máscara)': (capa_extra.copy(), "olvida la condición por completo"),
        f'"Pendiente" >= {umbral} (sin multiplicar por la capa)': (mascara.copy(), "olvida multiplicar por la capa"),
    }
    resultados = {k: v[0] for k, v in ops.items()}
    if not _distintos(*resultados.values()):
        return None
    nombre_correcta = f'("Pendiente" >= {umbral}) × "Capa extra"'
    resultado = resultados[nombre_correcta]
    opciones_op = _shuffle(rng, list(ops))
    distractores = [v for k, v in resultados.items() if k != nombre_correcta]
    opciones_res, indice_res = _shuffle_resultados(rng, resultado, distractores)
    return Pregunta(
        nivel=5,
        capas=[("Pendiente", pendiente), ("Capa extra", capa_extra)],
        operacion_nombre=nombre_correcta,
        operacion_formula=nombre_correcta,
        resultado=resultado,
        opciones_operacion=opciones_op,
        respuesta_operacion=nombre_correcta,
        opciones_resultado=opciones_res,
        indice_respuesta_resultado=indice_res,
        vmin_resultado=min(a.min() for a in resultados.values()),
        vmax_resultado=max(a.max() for a in resultados.values()),
    )


def _nivel_5_sindato(rng: np.random.Generator) -> Pregunta | None:
    capa_a = rng.integers(0, 2, size=(3, 3)).astype(float)
    capa_b = rng.integers(0, 2, size=(3, 3)).astype(float)
    fila_sd, col_sd = rng.integers(0, 3), rng.integers(0, 3)
    capa_a[fila_sd, col_sd] = np.nan

    correcto = np.minimum(capa_a, capa_b)  # NaN se propaga sola con np.minimum
    incorrecto = np.minimum(np.nan_to_num(capa_a, nan=0.0), capa_b)  # trata Sin Dato como 0

    if not _distintos(correcto, incorrecto):
        return None

    ops = {
        "AND propagando Sin Dato correctamente": (correcto, 'min("Capa A", "Capa B")'),
        "AND tratando Sin Dato como 0 (incorrecto)": (incorrecto, 'min("Capa A", "Capa B") tratando SD = 0'),
    }
    nombre_correcta = "AND propagando Sin Dato correctamente"
    opciones_op = _shuffle(rng, list(ops))
    opciones_res, indice_res = _shuffle_resultados(rng, correcto, [incorrecto])
    return Pregunta(
        nivel=5,
        capas=[("Capa A", capa_a), ("Capa B", capa_b)],
        operacion_nombre=nombre_correcta,
        operacion_formula=ops[nombre_correcta][1],
        resultado=correcto,
        opciones_operacion=opciones_op,
        respuesta_operacion=nombre_correcta,
        opciones_resultado=opciones_res,
        indice_respuesta_resultado=indice_res,
        vmin_resultado=0,
        vmax_resultado=1,
        categorical_capas=True,
        categorical_resultado=True,
        nodata=True,
    )


def generar_nivel_5(rng: np.random.Generator) -> Pregunta:
    variante = _nivel_5_mascara if rng.random() < 0.5 else _nivel_5_sindato
    for _ in range(MAX_INTENTOS):
        pregunta = variante(rng)
        if pregunta is not None:
            return pregunta
    raise RuntimeError("No se pudo generar una pregunta de nivel 5 sin distractores duplicados")


NIVELES = {
    1: generar_nivel_1,
    2: generar_nivel_2,
    3: generar_nivel_3,
    4: generar_nivel_4,
    5: generar_nivel_5,
}


def generar_pregunta(nivel: int, rng: np.random.Generator) -> Pregunta:
    nivel = max(1, min(5, nivel))
    return NIVELES[nivel](rng)
