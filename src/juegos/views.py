from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Juego

# Create your views here.

@api_view(["GET"])
def juegos(request):
    juegos = Juego.objects.all()
    #obtener los juegos
    return Response(juegos, status=status.HTTP_200_OK)