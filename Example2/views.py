from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#Importaciones de modelos
from Example2.models import Example2

#Importacion de Serializers
from Example2.serializer import Example2Serializers

class ExampleList(APIView):
    def get(self, request, format=None):
        print("GET")
        queryset = Example2.objects.all()
        serializer = Example2Serializers(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Example2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
            