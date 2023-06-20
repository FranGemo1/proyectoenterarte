# enterArte Backend

1. Para correr el proyecto instalar un entorno virtual:

```
pip install virtualenv

```
python -m virtualenv env  
```



2. Activar el entrno virtual:

```
./env/Scripts/activate
```

   

3. Quitar el ".dist" del titulo de del archivo `.env` dentro de la carpeta "core" y completar los campos con varibles de entorno de preferencia y las API Keys necesarias.
>>>>>>> develop

Con el entorno virtual activado, debemos intalar DJANGO y las librerias necesarias para el proyecto

Pueden instalar todo con el siguiente comando 
```
pip install -r requirements.txt
```
O también pueden instalarlos de la siguiente forma
```
pip install django djangorestframework django-cors-headers mysqlclient pillow django-rest-passwordreset django-allauth python-decouple
```

4. En caso de ser necesario realizar las migraciones correspondientes:


Para poder ejecutar el stack de backend, ademas de contar con Python instalado, es necesario una base de datos MySQL corriendo de nombre "enterarte".
>>>>>>> develop
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
  


5. Cuando traemos cambios a nuestro django hay que utilizar el siguiente comando para hacer las migraciones
```
py manage.py makemigrations
```
Correr el proyecto el servidor con el siguiente comando:
```
python manage.py runserver
```






