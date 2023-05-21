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

