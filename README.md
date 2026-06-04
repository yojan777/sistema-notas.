# Sistema de Notas

## Descripción
Sistema para calcular promedios y clasificar notas de estudiantes usando variables de entorno.

## Instalación
1. Clonar repositorio: `git clone https://github.com/yojan777/sistema-notas.git`
2. Crear entorno virtual: `python -m venv.venv`
3. Activar entorno: `.venv\Scripts\activate`
4. Instalar dependencias: `pip install -r requirements.txt`

## Variables de entorno
Copiar `.env.example` a `.env` y configurar:
- `APP_NAME`: Nombre de la aplicación
- `VERSION`: Versión actual
- `MAX_NOTA`: Nota máxima posible
- `MIN_APROBACION`: Nota mínima para aprobar

## Uso
```python
from notas import calcular_promedio, esta_aprobado, clasificar_nota

notas = [4.5, 3.8, 2.9, 4.0]
promedio = calcular_promedio(notas)
print(f"Promedio: {promedio}")
print(f"Aprobado: {esta_aprobado(promedio)}")
print(f"Clasificación: {clasificar_nota(promedio)}")