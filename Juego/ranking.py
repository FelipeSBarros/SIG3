"""Persistencia del ranking del juego, en SQLite (stdlib, sin dependencias nuevas).

Advertencia (ver `Juego/README.md`): en Streamlit Community Cloud el archivo `ranking.db` persiste
mientras la app siga activa, pero se reinicia en cada redeploy (push nuevo a git). Aceptable para un
juego de práctica, no para una calificación oficial.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "ranking.db"


def _conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(DB_PATH)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def init_db() -> None:
    with _conectar() as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS intentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                iniciado_en TEXT NOT NULL,
                puntaje INTEGER NOT NULL DEFAULT 0,
                nivel_alcanzado INTEGER NOT NULL DEFAULT 1,
                finalizado_en TEXT
            )
            """
        )


def registrar_inicio(nombre: str) -> int:
    """Guarda el nombre y la fecha/hora de un intento nuevo. Devuelve el id de esa fila."""
    ahora = datetime.now().isoformat(timespec="seconds")
    with _conectar() as conexion:
        cursor = conexion.execute(
            "INSERT INTO intentos (nombre, iniciado_en, puntaje, nivel_alcanzado) VALUES (?, ?, 0, 1)",
            (nombre.strip(), ahora),
        )
        return cursor.lastrowid


def actualizar_puntaje(intento_id: int, puntaje: int, nivel_alcanzado: int) -> None:
    ahora = datetime.now().isoformat(timespec="seconds")
    with _conectar() as conexion:
        conexion.execute(
            "UPDATE intentos SET puntaje = ?, nivel_alcanzado = ?, finalizado_en = ? WHERE id = ?",
            (puntaje, nivel_alcanzado, ahora, intento_id),
        )


def top_5() -> list[sqlite3.Row]:
    with _conectar() as conexion:
        conexion.row_factory = sqlite3.Row
        cursor = conexion.execute(
            """
            SELECT nombre, puntaje, nivel_alcanzado, iniciado_en
            FROM intentos
            WHERE finalizado_en IS NOT NULL
            ORDER BY puntaje DESC, iniciado_en ASC
            LIMIT 5
            """
        )
        return cursor.fetchall()
