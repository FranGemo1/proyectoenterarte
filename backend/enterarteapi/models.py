from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class Meta:
        app_label = 'enterarteapi',