from django.urls import path
from .views import juegos

urlpatterns = [
    path('', juegos, name="juegos_api"),
]
