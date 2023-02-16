# Alejandro Palmar Portafolio
<p align= center>
<img src="https://i.postimg.cc/GtDBtjMp/Group-21-1.png">
</p>

Portafolio trabajado con Django, para poder utilizarlo primero debes clonar el repositorio con el siguiente comando:

git clone https://github.com/ThePalmars1one/portfolio.git

Debes verificar si tienes "pip" instalado, si tienes python 2.7.9 o una versión mayor, pip viene instalado por defecto.

## VENV
Después de clonarlo debes crear el entorno virtual con el siguiente comando y luego activarlo:

1. python -m venv venv_name

2. source venv_name/Scripts/activate (GIT BASH)

## Requirements.txt
En el repositorio se encuentran todos los paquetes necesarios para que el proyecto funcione, los cuales instalarás con el siguiente comando:

1. pip install -r requirements.txt

# Apps
El proyecto cuenta con dos aplicaciones: Technologies y Projects

## Projects
A continuación el modelo de la app projects, donde "title" y "description" tienen una longitud máxima aceptada de caracteres de 100, "image" utiliza ImageField para poder recibir una imagen y "link" se da la especificación de blank=True para que no sea obligatorio colocar un enlace en el mismo.

<p>
<img src="https://i.postimg.cc/zGvkDsCD/project-models.png">
</p>

En cuanto a las vistas se importan los modelos de ambas aplicaciones para poder trabajar sobre un mismo template.

<p>
<img src="https://i.postimg.cc/jjmTkYXD/views-projects.png">
</p>

## Technologies
El modelo de Technologies tiene la particularidad de que no utiliza ImageField sino FileField, esto debido a que FileField tiene menos limitaciones en cuanto al tipo de archivos que puede recibir, ya que por ejemplo "ImageField" no acepta archivos con la extensión ".svg"

<p>
<img src="https://i.postimg.cc/fRy64gkm/tech-models.png">
</p>

## Settings
Configuraciones adicionales para que la app general pueda recibir distintas extensiones, establecer "media" para que las imágenes se guarden de manera pública y "static" para todos los archivos estáticos del proyecto como los estilos, entre otros.

<p>
<img src="https://i.postimg.cc/MT5DpqFT/settings.png">
</p>

## Test
El siguiente es uno de los dos tests realizados, donde el código verifica la creación de un proyecto:

<p>
<img src="https://i.postimg.cc/KjtF8Cvp/test.png">
</p>

y por último el resultado por consola:

<p>
<img src="https://i.postimg.cc/mDwyWg7m/consola-test.png">
</p>

