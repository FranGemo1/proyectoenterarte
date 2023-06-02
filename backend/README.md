
### BackEnd:


Luego de clonar el repositorio sera necesario crear un entorno virtual, por lo que es necesario instalar virtualenv:

```
pip install virtualenv
```
Le decimos a Python que vamos a usar un entorno virtual y que cree la carpeta “venv“ para contenerlo:
```
python -m virtualenv venv
```
Activamos el entorno virtual, en windows ```.\venv\Scripts\activate```, en linux ```./venv/Scripts/activate```

Con el entorno virtual activado, debemos intalar DJANGO y las librerias necesarias para el proyecto

Pueden instalar todo con el siguiente comando 
```
pip install -r requirements.txt
```
O también pueden instalarlos de la siguiente forma
```
pip install django djangorestframework django-cors-headers mysqlclient pillow django-rest-passwordreset django-allauth python-decouple
```

Para poder ejecutar el stack de backend, ademas de contar con Python instalado, es necesario una base de datos MySQL corriendo de nombre "enterarte". Una manera sencilla de tener una base de datos mySQL es mediante Docker, que una vez instaldo solo sera necesario ejecutar el siguiente comandos

```
docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql
```

Ahora podemos abrir una nueva terminal y ejecutar los siguientes comandos para ingresar a la base de datos desde docker
```
docker exec -it mysql bash
```
```
mysql -u root -p 
```
Nos deberia pedir la contraseña.


En el bash de MySQL ejecutamos los siguientes comandos
```
CREATE DATABASE enterarte;
```
```
USE enterarte;
```


Listo tenemos nuestra base de datos creada y seleccionada podemos volver a la terminal en la que tenemos el entorno virtual de Python y ejecutamos el siguiente comando para hacer las migraciones que crean la estructura de la base de datos
```
py manage.py migrate
```


Podemos volver al Bash de MySQL y ejecutar `show tables;` y deberiamos obtener algo similar a lo siguiente que confirman la estructura de la base de datos



Nuevamente en nuestro entorno virtual pasaremos a crear un superusuario con el siguiente comando

```py manage.py createsuperuser```, Nos pedira un usuario un password, la confirmación del password y un correo

Una ves creado el usuario volvemos a activar el servidor, ``` py manage.py runserver```, nos dejara una ip con un puerto por defecto y es  ```http://127.0.0.1:8000/```, la copiamos y pegamos en el navegador

Cuando accedemos a la ip por defecto ```http://127.0.0.1:8000/ ``` veremos que django esta corriendo correctamente

Para acceder al panel de django agregamos  ```/admin ``` a la ip quedaria así,  ```http://127.0.0.1:8000/admin ```, nos logueamos con el usuario y el password recientemente creados

Cuando traemos cambios a nuestro django hay que utilizar el siguiente comando para hacer las migraciones
```
py manage.py makemigrations
```





