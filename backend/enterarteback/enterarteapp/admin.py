from django.contrib import admin
from .models import Eventos, EventosData, Permisos, Roles, Ticket, UserData, Users

# Register your models here.

@admin.site.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    pass

@admin.site.register(EventosData)
class EventosDataAdmin(admin.ModelAdmin):
    pass

@admin.site.register(Permisos)
class PermisosAdmin(admin.ModelAdmin):
    pass

@admin.site.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass

@admin.site.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.site.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    pass

@admin.site.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
