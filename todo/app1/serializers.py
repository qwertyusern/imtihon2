from rest_framework import serializers
from .models import *

class TodoSer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
