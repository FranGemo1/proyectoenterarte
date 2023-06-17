from django.apps import AppConfig


class EnterarteappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enterarteapp'
    
    def ready(self):
        import enterarteapp.signals  # Importa las señales
