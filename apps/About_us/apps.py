from django.apps import AppConfig


class WorkerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.About_us'
    verbose_name = 'О нас'
    def ready(self):
        import apps.About_us.signal
