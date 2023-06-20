from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxValueValidator
from .validators import *
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created 
from django.core.mail import send_mail 
from django import random
# Create your models here.
class CustomUserManager(BaseUserManager): #para que el usuario se pueda loguear con el email
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio") #si no se ingresa un email
        
        email = self.normalize_email(email) #normalizar el email
        user = self.model(email=email, **extra_fields) #crear el usuario
        user.set_password(password) #setear la contraseña
        user.save(using=self._db) #guardar el usuario
        return user #devolver el usuario

    def create_superuser(self, email, password=None, **extra_fields): #crear un superusuario
        extra_fields.setdefault('is_staff', True) #si no se ingresa un valor para is_staff, se establece en True
        extra_fields.setdefault('is_superuser', True) #si no se ingresa un valor para is_superuser, se establece en True
        
        if extra_fields.get('is_staff') is not True: #si is_staff no es True
            raise ValueError('Superuser must have is_staff=True.') #se lanza un error
        if extra_fields.get('is_superuser') is not True: #si is_superuser no es True
            raise ValueError('Superuser must have is_superuser=True.') #se lanza un error

        return self.create_user(email, password, **extra_fields) #se crea el superusuario

class Client(AbstractUser): #modelo de usuario personalizado
    username = None #se establece el username en None
    password = models.CharField(max_length=128, default=make_password('default_password'))
    email = models.EmailField(unique=True, default='example@example.com') #se establece el email como campo unico
    phone = models.CharField(max_length=15, null=True, blank=True, validators=[phone_valid]) #maximo 15 caracteres y validacion
    address = models.CharField(max_length=100, null=True, blank=True, validators=[address_valid]) #maximo 100 caracteres y validacion
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, validators=[validate_image]) #campo para subir imagenes con validacion
        
    USERNAME_FIELD = 'email' #se establece el email como campo de autenticacion
    REQUIRED_FIELDS = ['first_name', 'last_name'] #se establecen los campos requeridos
    
    objects = CustomUserManager() #se establece el objeto CustomUserManager como objeto de la clase User
    
    groups = models.ManyToManyField( #se establece la relacion de muchos a muchos con la tabla Group
        'auth.Group',
        verbose_name='groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField( #se establece la relacion de muchos a muchos con la tabla Permission
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
    )
    
    class Meta: #metadatos
        verbose_name = 'Cliente' #nombre en singular
        verbose_name_plural = 'Clientes' #nombre en plural
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" #concatenar el primer nombre y el apellido
    
    def get_short_name(self): 
        return self.first_name




class Category(models.Model):
    name = models.CharField(max_length=50, validators=[name_valid]) #maximo 50 caracteres y validacion
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: #metadatos
        verbose_name = 'Categoría' #nombre en singular
        verbose_name_plural = 'Categorías' #nombre en plural
        
    def __str__(self):
        return self.name
    
    
class Review(models.Model): #modelo de review
    client = models.ForeignKey(Client, on_delete=models.CASCADE) #relacion de uno a uno con la tabla Client
    description = models.CharField(max_length=140) #maximo 140 caracteres
    classification = models.IntegerField(validators=[MaxValueValidator(5)], default=1) #solo numeros positivos por defecto 1 y maximo 5
    created_at = models.DateTimeField(auto_now_add=True) #fecha de creacion
    
    class Meta: #metadatos
        verbose_name = 'Reseña' #nombre en singular
        verbose_name_plural = 'Reseñas' #nombre en plural

    def __str__(self):
        return str(self.id)    
    
    
    
class Article(models.Model): #modelo de articulo
    name = models.CharField(max_length=50, validators=[name_valid]) #maximo 50 caracteres y validacion
    description = models.CharField(max_length=100) #maximo 100 caracteres
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #relacion de uno a uno con la tabla Category
    price = models.DecimalField(max_digits=10, decimal_places=0) # maximo 10 digitos y 0 decimales
    stock = models.PositiveIntegerField(default=1) #solo numeros positivos por defecto 1
    image = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image]) #campo para subir imagenes con validacion
    review = models.ManyToManyField(Review, blank=True) #relacion de muchos a muchos con la tabla Review (opcional)
    created_at = models.DateTimeField(auto_now_add=True) #fecha de creacion
    
    class Meta: #metadatos
        verbose_name = 'Artículo' #nombre en singular
        verbose_name_plural = 'Artículos' #nombre en plural    
    

    def __str__(self):
        return self.name
    
class Coment(models.Model): #modelo de comentario
    client = models.ForeignKey(Client, on_delete=models.CASCADE) #relacion de uno a uno con la tabla Client
    description = models.CharField(max_length=140) #maximo 140 caracteres
    classification = models.IntegerField(validators=[MaxValueValidator(5)], default=1) #solo numeros positivos por defecto 1 y maximo 5
    created_at = models.DateTimeField(auto_now_add=True) #fecha de creacion    

    class Meta: #metadatos
            verbose_name = 'Comentario' #nombre en singular
            verbose_name_plural = 'Comentarios' #nombre en plural

    def __str__(self):
        return str(self.id)


class Cart(models.Model): #modelo de carrito
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    products = models.ManyToManyField(Article, through='CartDetail') #relacion muchos a muchos con la tabla CartDetail
    confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    def set_confirm(self, *args, **kwargs):
        for i in self.products.all():
            if i.item.stock < i.quantity:
                return False
        self.confirm = True
        super().save(*args, **kwargs)

class CartDetail(models.Model): #modelo de detalle de carrito
    item = models.ForeignKey(Article, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return str(self.id)

    #reescribir el metodo save para que se actualice el precio total del pedido cada vez que se agregue un producto
    def save(self, *args, **kwargs): 
        self.amount = self.item.price * self.quantity
        super().save(*args, **kwargs)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title

class Meta:
    app_label = 'enterarte',


        
# Create your models here.

    
class UserData(models.Model):
    id_user_data=models.AutoField(int, primary_key=True)
    name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=50)
    birthday=models.DateField()
    phone=models.CharField(max_length=20)
    id_user=models.ForeignKey("User", to_field="id_user", on_delete=models.CASCADE)
    
class User(models.Model):
    id_user=models.AutoField(int, primary_key=True)
    id_user_data=models.ForeignKey("UserData", to_field="id_user_data", on_delete=models.CASCADE)
    id_rol=models.ForeignKey("Roles", to_field="id_rol", on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=20)

    
    
class Permissions(models.Model):
    id_permission=models.AutoField(int, primary_key=True)
    restrictions=models.CharField(max_length=20)
    id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
    
    
class EventsData(models.Model):
    id_event_data=models.AutoField(int, primary_key=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=250)
    date=models.DateField()
    photo=models.ImageField(upload_to="Galeria", null=False, blank=False, default=None)
    category=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    province=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    number=models.IntegerField()
    socialNetworks=models.CharField(max_length=20)
    id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)


class Events(models.Model):
    id_event=models.AutoField(int, primary_key=True)
    id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
    id_ticket=models.ForeignKey("Ticket",to_field="id_ticket", on_delete=models.CASCADE)


def generate_random_min_value():
    # Generar un valor mínimo aleatorio entre 10000 y 100250000 (puedes ajustarlo según se requiera)
    return random.randint(10000, 250000)

class Ticket(models.Model):    
    id_ticket=models.IntegerField(validators=[MinValueValidator(limit_value=generate_random_min_value), MaxValueValidator(25000000)],unique=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    dateTime=models.DateTimeField()
    id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
    
    def clean(self):
        # Realizar la validación de unicidad del número de ticket
        if Ticket.objects.exclude(id=self.id).filter(id_ticket=self.id_ticket).exists():
            raise ValidationError('El número de ticket ya existe.')

class TransactionReport(models.Model):
    id_report=models.AutoField(int, primary_key=True)
    id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
    id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
    id_order=models.ForeignKey("ShoppingOrder", to_field="id_order",on_delete=models.CASCADE)
    

class ShoppingOrder(models.Model):
    id_order=models.AutoField(int, primary_key=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    dateTime=models.DateTimeField()
    id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
    id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
            
    
class Roles(models.Model):
    id_rol=models.AutoField(int, primary_key=True)
    rol=models.CharField(max_length=15,blank=False)
    id_user=models.ForeignKey("User", to_field="id_user", on_delete=models.CASCADE)
    id_permission=models.ForeignKey("Permissions", to_field="id_permission", on_delete=models.CASCADE)        
