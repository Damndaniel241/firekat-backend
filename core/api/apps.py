from django.apps import AppConfig
# import importlib

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # def ready(self):
    #     # import api.signals
    #     importlib.import_module('api.signals')




