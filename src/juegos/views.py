from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Juego
from .serializers import JuegoSerializer

# Create your views here.

@api_view(["GET", "POST"])
def juegos(request):
    if request.method == "GET":
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos, many=True)
        #obtener los juegos
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = JuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje":"Juego creado"}, status=status.HTTP_201_CREATED)
        return Response({"mensaje":"No se creo porque no es valido"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def juegos_detail(request, pk):
    if request.method == "GET":
        juego = get_object_or_404(Juego, pk=pk)
        serializer = JuegoSerializer(juego)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        juego = get_object_or_404(Juego, pk=pk)
        serializer = JuegoSerializer(juego, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje":"Juego actualizado"}, status=status.HTTP_200_OK
            )
        return Response(
            {"mensaje": "No se actualizo porque no es valido"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if request.method == "DELETE":
        juego = get_object_or_404(Juego, pk=pk)
        juego.delete()
        return Response(
            {"mensaje": "juego borrado"},
            status=status.HTTP_200_OK
        )
        