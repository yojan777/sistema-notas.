import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Lee las variables
APP_NAME = os.getenv("APP_NAME", "SistemaNotas")
VERSION = os.getenv("VERSION", "1.0.0")

# Convierte a float y valida
try:
    MAX_NOTA = float(os.getenv("MAX_NOTA", 5.0))
    MIN_APROBACION = float(os.getenv("MIN_APROBACION", 3.0))
except ValueError:
    raise ValueError("MAX_NOTA y MIN_APROBACION deben ser números")

# Validaciones que pide el profe
if not 0 < MIN_APROBACION <= MAX_NOTA:
    raise ValueError(f"MIN_APROBACION debe estar entre 0 y {MAX_NOTA}")

if MAX_NOTA <= 0:
    raise ValueError("MAX_NOTA debe ser mayor a 0")

print(f"Config cargada: {APP_NAME} v{VERSION}")
print(f"Nota máxima: {MAX_NOTA} | Nota mínima aprobación: {MIN_APROBACION}")
