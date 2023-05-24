from django.db import models

class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    id_User = models.ForeignKey(User,to_field="id_User",on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

class Meta:
        app_label = 'enterarteapp',


#Models User

class User(models.User):
    id_User = models.AutoField(primary_key=True)
    name = models.Charfield(max_length=100, blank=False)
    lastname = models.Charfield(max_length=100, blank=False)
    user = models.Charfield(max_length=100, blank=False)
    password = models.Charfield(max_length=100, blank=False)
    class Meta:
        db_table="User"
        verbose_name="Date users"
        verbose_name_plural="Users"
    def __unicode__(self):
        return self.user
    def __str__(self):
        return self.user        


# import random
# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.core.exceptions import ValidationError

# # Create your models here.

    
# class UserData(models.Model):
#     id_user_data=models.AutoField(int, primary_key=True)
#     name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=50)
#     birthday=models.DateField()
#     phone=models.CharField(max_length=20)
#     id_user=models.ForeignKey("User", to_field="id_user", on_delete=models.CASCADE)
    
# class User(models.Model):
#     id_user=models.AutoField(int, primary_key=True)
#     id_user_data=models.ForeignKey("UserData", to_field="id_user_data", on_delete=models.CASCADE)
#     id_rol=models.ForeignKey("Roles", to_field="id_rol", on_delete=models.CASCADE)
#     email = models.EmailField(unique=True, blank=False)
#     password = models.CharField(max_length=20)

    
    
# class Permissions(models.Model):
#     id_permission=models.AutoField(int, primary_key=True)
#     restrictions=models.CharField(max_length=20)
#     id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
    
    
# class EventsData(models.Model):
#     id_event_data=models.AutoField(int, primary_key=True)
#     title=models.CharField(max_length=20)
#     description=models.CharField(max_length=250)
#     date=models.DateField()
#     photo=models.ImageField(upload_to="Galeria", null=False, blank=False, default=None)
#     category=models.CharField(max_length=50)
#     gender=models.CharField(max_length=20)
#     province=models.CharField(max_length=50)
#     location=models.CharField(max_length=50)
#     street=models.CharField(max_length=50)
#     number=models.IntegerField()
#     socialNetworks=models.CharField(max_length=20)
#     id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
    

# class Events(models.Model):
#     id_event=models.AutoField(int, primary_key=True)
#     id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
#     id_ticket=models.ForeignKey("Ticket",to_field="id_ticket", on_delete=models.CASCADE)
         

# def generate_random_min_value():
#     # Generar un valor mínimo aleatorio entre 10000 y 100250000 (puedes ajustarlo según se requiera)
#     return random.randint(10000, 250000)

# class Ticket(models.Model):    
#     id_ticket=models.IntegerField(validators=[MinValueValidator(limit_value=generate_random_min_value), MaxValueValidator(25000000)],unique=True)
#     price=models.DecimalField(max_digits=20,decimal_places=2)
#     dateTime=models.DateTimeField()
#     id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
    
#     def clean(self):
#         # Realizar la validación de unicidad del número de ticket
#         if Ticket.objects.exclude(id=self.id).filter(id_ticket=self.id_ticket).exists():
#             raise ValidationError('El número de ticket ya existe.')

# class TransactionReport(models.Model):
#     id_report=models.AutoField(int, primary_key=True)
#     id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
#     id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
#     id_order=models.ForeignKey("ShoppingOrder", to_field="id_order",on_delete=models.CASCADE)
    

# class ShoppingOrder(models.Model):
#     id_order=models.AutoField(int, primary_key=True)
#     price=models.DecimalField(max_digits=10,decimal_places=2)
#     dateTime=models.DateTimeField()
#     id_user=models.ForeignKey("User",to_field="id_user", on_delete=models.CASCADE)
#     id_event=models.ForeignKey("Events",to_field="id_event", on_delete=models.CASCADE)
            
    
# class Roles(models.Model):
#     id_rol=models.AutoField(int, primary_key=True)
#     rol=models.CharField(max_length=15,blank=False)
#     id_user=models.ForeignKey("User", to_field="id_user", on_delete=models.CASCADE)
#     id_permission=models.ForeignKey("Permissions", to_field="id_permission", on_delete=models.CASCADE)        