from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base_app"
    verbose_name = "Research Hub"
