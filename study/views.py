from rest_framework.decorators import api_view

from .models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response

@api_view(["GET"])
def StudentView(request):
    qs = Students.objects.all()
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)
    