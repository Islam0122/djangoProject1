import os
import sys

from django.core.wsgi import get_wsgi_application

# Путь к вашему Django проекту
path = '/home/islam24/djangoProject1/djangoProject1'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')
application = get_wsgi_application()