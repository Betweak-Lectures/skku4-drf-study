# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Students, Score

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["name", "address", "email"]

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["student", "english", 
                  "math", "science", "exam_date"]
    