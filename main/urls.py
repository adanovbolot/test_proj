from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)