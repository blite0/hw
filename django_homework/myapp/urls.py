from django.urls import path
from .views import first
from django.contrib import admin


urlpatterns = [
    path('', first),
    path('admin/', admin.site.urls),
]
