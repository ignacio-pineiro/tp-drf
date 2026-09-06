# tp-drf

Uso de uv en biblioteca de juegos


# Instalación de entorno uv:

--> Primero se instala el uv si no lo tienen:
     - curl -LsSf https://astral.sh/uv/install.sh | sh

--> Reiniciamos la terminal

--> Entramos a la carpeta del proyecto-django y corremos:
     - uv add django
     - uv add djangorestframework


# Para hacer las migraciones:

--> En la carpeta src del proyecto:
     - uv run manage.py makemigrations
     - uv run manage.py migrate


# Para correr el servidor:

--> En la terminal en la carpeta src:
     - uv run manage.py runserver