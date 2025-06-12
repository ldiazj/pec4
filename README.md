# PEC4 - Proyecto Python

## Descripción

Proyecto en python para la practica 4 de la asignatura de programación.

## Estructura del proyecto

<pre>
pec4/  
├── doc/                    # Documentación del proyecto  
    └── src/  
        └── index.html      # Página principal de la documentación  
    └── dataset.csv         # Fichero con los datos para la practica  
├── img/                    # Imágenes generadas en el practica  
├── screenshots/            # Capturas de pantalla de la solución  
├── src/                    # Código fuente del proyecto  
    └── exercise  
        └── first.py        # Módulo para el primer ejecrcicio  
        └── second.py       # Módulo para el segundo ejercicio  
        └── third.py        # Módulo para el tercero ejercicio  
        └── fourth.py       # Módulo para el cuarto ejercicio  
        └── fifth.py        # Módulo para el quinto ejercicio  
    └── main.py             # Archivo principal del proyecto  
├── tests/                  # Pruebas del proyecto  
    └──__init__.py          # Archivo de inicialización del paquete  
    └── test_first.py       # Pruebas para el primer ejercicio  
    └── test_second.py      # Pruebas para el segundo ejercicio  
    └── test_third.py       # Pruebas para el tercero ejercicio  
    └── test_fourth.py      # Pruebas para el cuarto ejercicio  
    └── test_fifth.py       # Pruebas para el quinto ejercicio  
├── .pylintrc               # Archivo configuracion Pylint  
├── LICENSE.txt             # Archivo con la licencia  
├── NOTICE.txt              # Archivo con las dependencias
├── README.md               # Archivo que estás leyendo  
├── setup.py                # Script de configuración del proyecto  
├── requirements.txt        # Dependencias del proyecto
</pre>

## Entorno virtual

### Crear entorno virtual

virtualenv .venv

### Activar entorno virtual

source .venv/Scripts/activate

## Instalación paquetes

pip install -r requirements.txt

## Ejecución del programa

python src/main.py [-h | --help] [-ex N]

N indica hasta que numero de ejercicio se quiere ejecutar.

## Testing y cobertura

### Ejecutar los test

pytest tests/

### Cobertura de código

pytest --cov=src tests/

## Generar documentación

Si es la primera vez que se genera hay que definir el src como módulo principal y es necesario ejecutar lo siguiente:

export PYTHONPATH=src

Para la generación.

pdoc --html src --output-dir doc

En el caso de ya existir el html se fuerza la creación.

pdoc -f --html src --output-dir doc

Luego se abre el documento doc/src/index.html en el navegador.

## Linter (PEP8)

pylint src/

## Repositorio GitHub

https://github.com/ldiazj/pec4.git
