from django.contrib import admin
from .models import User
from .models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=("title", "descripcion", "price")

class UserAdmin(admin.ModelAdmin):
    list_display=("user")

admin.site.register(Event,EventAdmin)
admin.site.register(User,UserAdmin)