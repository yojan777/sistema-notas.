import os
from dotenv import load_dotenv

load_dotenv()

MAX_NOTA = float(os.getenv("MAX_NOTA"))
MIN_APROBACION = float(os.getenv("MIN_APROBACION"))


def calcular_promedio(notas: list[float]) -> float:
    """
    Calcula el promedio de una lista de notas.

    Args:
        notas (list[float]): Lista de notas numéricas.

    Returns:
        float: Promedio de las notas.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def esta_aprobado(nota: float) -> bool:
    """
    Determina si una nota está aprobada según MIN_APROBACION del.env.

    Args:
        nota (float): Nota a evaluar.

    Returns:
        bool: True si está aprobada, False si no.
    """
    return nota >= MIN_APROBACION


def clasificar_nota(nota: float) -> str:
    """
    Clasifica una nota en Excelente, Bueno, Regular o Deficiente.
    Usa MAX_NOTA del.env para el cálculo.

    Args:
        nota (float): Nota a clasificar.

    Returns:
        str: Clasificación de la nota.
    """
    if nota >= MAX_NOTA * 0.9:
        return "Excelente"
    elif nota >= MAX_NOTA * 0.7:
        return "Bueno"
    elif nota >= MIN_APROBACION:
        return "Regular"
    else:
        return "Deficiente"
