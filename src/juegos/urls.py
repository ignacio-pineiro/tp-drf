from django.urls import path
from .views import juegos, juegos_detail

urlpatterns = [
    path('', juegos, name="juegos_api"),
    path("<int:pk>/", juegos_detail, name="juego_detail_api")
]
