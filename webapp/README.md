# CONCIENCIA SONORA - WEBAPP

## Caracteristicas

* **Diseño -** Diseño basado en [HTML5](https://developer.mozilla.org/es/docs/HTML/HTML5), [CSS3](https://developer.mozilla.org/es/docs/Web/CSS) y [Bootstrap4](https://getbootstrap.com/). Se usa [Flask](http://flask.palletsprojects.com/en/1.1.x/) y [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) para crear los templates.
* **Administración de sesiones -** La validacion de datos enviados al servidor (usuario, contraseña y email) es mediante [Python](https://www.python.org/). Se almacenan todos los datos de las sesiones en una base de datos relacional.
* **MySQL Queries -** *Select*, *Insert* almacenados desde/hacia las tablas de la base de datos.
* **Rutas -** Se asignan funciones a las rutas de la webApp, utilizando Flask.

## Descargar repositorio

**Con `git`**
Si tiene instalado git, la forma más fácil de acceder a estos archivos es clonar el repositorio en el directorio que elija.

``` bash
git clone https://github.com/infiniemlabs-acustica/conciencia-sonora.git
```

**Sin `git`**
Alternativamente, puede descargar todo el repositorio como un archivo .zip desde la página de inicio del repositorio utilizando el botón verde "Clonar o descargar" en la esquina superior derecha.

## Requerimientos

1. Python (> v3.x). Se recomienda instalar [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. XAMPP.

### Paquetes

``` bash
pip install -r requirements.txt
``` 


## Referencias

El desarrollo fue inspirado en el tutorial de [David Adams](https://codeshack.io/author/david-adams/) de [CodeShack](https://codeshack.io/author/david-adams/), *[Login System with Python Flask and MySQL](https://codeshack.io/login-system-python-flask-mysql/)*.

