from rest_framework.decorators import api_view
from rest_framework.views import APIView


from .models import Students, Score
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response

from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count, F, Value


##  Function Based View
@api_view(['GET', 'POST'])
def StudentView(request):
    if request.method == 'GET':
      qs = Students.objects.all() # 데이터 조회
      serializer = StudentSerializer(qs, many=True)
      return Response(serializer.data)
    elif request.method == 'POST':
      serializer = StudentSerializer(data=request.data) # serializer 
      
      if serializer.is_valid(): # validation check
        serializer.save() # save data to model 
        return Response(serializer.data, status.HTTP_201_CREATED)

      return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, pk):
  qs = get_object_or_404(Students, pk=pk)
  
  if request.method == 'GET':
    serializer = StudentSerializer(qs)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = StudentSerializer(qs, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    qs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class StudentView(APIView):
    """
    Class Based View

    url: /students

    - get: 학생 목록조회
    - post: 학생등록
    """
    def get(self, request):
        qs = Students.objects.all()
        # qs = Students.objects.filter().all()  # 데이터 조회
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)  # serializer

        if serializer.is_valid():  # validation check
            serializer.save()  # save data to model
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    """
    CBV
    url: /students/<int:pk>

    - get: pk 학생 세부조회
    - put: pk 학생 수정
    - delete: pk 학생 삭제
    """
    
    def get_object(self, pk):
        return get_object_or_404(Students, pk=pk)
    

    def get(self, request, pk):
        qs = self.get_object(pk)
        
        

        serializer = StudentSerializer(qs)
        return Response(serializer.data)

    def put(self, request, pk):
        qs = self.get_object(pk)

        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = self.get_object(pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)













# @api_view(["GET"])
# def StudentView(request):
#     """학생들 조회하는 API"""
#     qs = Students.objects.all()
#     serializer = StudentSerializer(qs, many=True)
#     return Response(serializer.data)

# @api_view(["GET"])
# def ScoreView(request):
#     qs = Score.objects.all()
#     serializer = ScoreSerializer(qs, many=True)
#     return Response(serializer.data)


# score 리스트 조회 및 추가
@api_view(['GET', 'POST'])
def ScoreView(request):
    if request.method == 'GET':
        qs = Score.objects.all()  # 데이터 전체 조회
        serializer = ScoreSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# score 상세조회, 수정, 삭제


@api_view(['GET', 'PUT', 'DELETE'])
def ScoreDetailView(request, pk):
    qs = get_object_or_404(Score, pk=pk)

    if request.method == 'GET':
        serializer = ScoreSerializer(qs)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ScoreSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def StudentScoreView(request, pk):
    qs = get_object_or_404(Students, pk=pk)

    if request.method == 'GET':
        scores = qs.score_set.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScoreSerializer(data={'student': qs.pk, **request.data})
        if serializer.is_valid():
            serializer.save()
            # score = Score(**serializer.data, student=qs).save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SampleView(APIView):
#     queryset = Students.objects.all()
#     serializer = StudentSerializer
    
#     def list(self, request):
#         # GET /url
        
#         return Response(StudentSerializer(self.queryset, many=True).data)
    
#     def create(self, request):
#         # POST /url
#         serializer = StudentSerializer(data=request.data).save()
        
#         return Response(serializer.data)
    
#     def destroy(self, request, pk):
#         # DELETE /url/<pk>
#         self.queryset.filter(pk=pk).first().delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def retrieve(self, request, pk):
#         # GET /url/<pk>
#         return Response(serializer = StudentSerializer(self.queryset.filter(pk=pk).first()))
    
#     def update(self, request, pk):
#         # GET /url/<pk>
#         serializer = StudentSerializer(instance = self.queryset.filter(pk=pk).first())
#         if serializer.is_valid():
#             serializer.update(**request.data)
#         return Response(serializer.data)
    


from rest_framework import viewsets
from rest_framework.decorators import action



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name).all()
        return qs
    
    @action(["GET"], detail=False)
    def incheon(self, request):
        qs = self.get_queryset()
        qs = qs.filter(address__contains="인천")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

from django.db.models import F
from django.db.models.lookups import GreaterThan

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    
    """
    score 모델에 name 및 각 점수별 검색조건을 추가해주세요.

    1. name parameter가 있을경우 이름이 일치하는 사람을 검색해주세요.
    2. 각 과목별로 점수 parameter를 넣으면 해당과목이 전달한 점수보다 높은 학생만 조회해주세요.
    3. ‘order’ parameter가 있을경우 해당 parameter값으로 정렬해주세요.
    """
    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        
        if name:
            qs = qs.filter(student__name=name).all()
            
        score_list = ["math", "english", "science"]
        for score in score_list:
            qs = self.filter_score(qs, score)
            
        order = self.request.query_params.get('order')
        if order:
            qs = qs.order_by(order)
        return qs
    
    def filter_score(self, qs, param_key):
        name = self.request.query_params.get(param_key)
        if name:
            qs = qs.filter(**{f'{param_key}__gte': name})
        return qs
    
    @action(methods=["GET"], detail=False)
    def top(self, request):
        # score 서비스에 /top 을 넣으면 모든점수의 합이
        # 270점이 넘는사람만 조회해주세요
        
        qs = self.get_queryset().filter(
            GreaterThan(F("math")+F("science")+F("english"), 270)
        )
        serializer = self.get_serializer(instance=qs, many=True)
        
        return Response(serializer.data)
        
    
    
    
    
    