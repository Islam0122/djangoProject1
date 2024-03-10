import os
import sys

from django.core.asgi import get_asgi_application

path = '/home/islam24/djangoProject1/djangoProject1'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

application = get_asgi_application()
