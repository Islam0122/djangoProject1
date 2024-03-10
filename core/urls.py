from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/about_us/', include('apps.About_us.urls')),
                  path('api/v1/contact/', include('apps.Contact.urls')),
                  path('api/v1/galereya/', include('apps.Galereya.urls')),
                  path('api/v1/menu/', include('apps.Menu.urls')),
                  path('api/v1/news/', include('apps.News.urls')),
                  path('api/v1/service/', include('apps.Service.urls')),
                  path('api/v1/qr_code/', include('apps.QR_code.urls')),

              ] + urls_swagger
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)