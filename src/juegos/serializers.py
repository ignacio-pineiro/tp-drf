from rest_framework import serializers
from .models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = [
            "id",
            "titulo",
            "plataforma",
            "fecha_lanzamiento",
            "precio",
        ]
        read_only_fields= ["id"]