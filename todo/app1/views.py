from django.shortcuts import render
from rest_framework import viewsets

from.serializers import *
from .models import *
class TodoVS(viewsets.ModelViewSet):
    serializer_class = TodoSer
    queryset = Todo.objects.all()