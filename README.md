Abrir CMD desde la carpeta

Crear un entorno virtual para no afectar toda la maquina:
Entorno virtual para python:
python -m venv env

Una vez instalado el entorno virtual activarlo desde CMD con la opcion 1

opcion 1:
env\scripts\activate

opcion 2:   Esta opcion es para desactivarla, no usarla de momento
env\scripts\deactivate

Instalar requerimientos de texto requirements.txt:
pip install -r requirements.txt

Una vez instalados los requerimientos, escribir lo siguiente en el CMD para correr el programa
streamlit run app.py