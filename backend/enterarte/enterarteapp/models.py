from django.db import models

# Create your models here.
import random
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created 
from django.core.mail import send_mail 

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0) # maximo 10 digitos y 0 decimales
    stock = models.PositiveIntegerField(default=1) #solo numeros positivos por defecto 1
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def getEmail(self):
        return f"{self.user.email}"
    
    def save(self, *args, **kwargs):
        # Concatenate el primer name y el lastName para set el campo name
        self.name = f"{self.user.first_name} {self.user.last_name}"
        # Llamar al método save del modelo padre para guardar los cambios
        super().save(*args, **kwargs)
    
    def __str__(self):
            return self.name

class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
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

class CartDetail(models.Model):
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



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs): #obtiene el token

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail( #envia el mail
        # title:
        "Password Reset for {title}".format(title="Restablecer Contraseña"),#un titulo
        # message:
        email_plaintext_message,
        # from:
        "enterspace.ar@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


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
