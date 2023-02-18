from django.apps import AppConfig


class BaseBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_backend'
