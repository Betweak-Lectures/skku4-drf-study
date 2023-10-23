# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Students, Score

class ScoreListField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'math': value.math,
            'english': value.english,
            'science': value.science
        }


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["name", "address", "email", 'score_set']
        
    score_set = ScoreListField(many=True, read_only=True)


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["student", "english", 
                  "math", "science", "exam_date"]
    student = StudentSerializer()
    
