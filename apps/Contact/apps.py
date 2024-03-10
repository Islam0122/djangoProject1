from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Contact'
    verbose_name = 'Контакты'
    def ready(self):
        import apps.Contact.signal

