from rest_framework.decorators import api_view

from .models import Students, Score
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response

@api_view(["GET"])
def StudentView(request):
    """학생들 조회하는 API"""
    qs = Students.objects.all()
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def ScoreView(request):
    qs = Score.objects.all()
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data)