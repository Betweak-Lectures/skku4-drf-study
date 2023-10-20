# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["name", "address", "email"]

