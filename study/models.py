from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)


# score 모델을 추가해주세요.
# 학생들은 총 여러번의 시험을 볼 수 있습니다.
# 컬럼을 english, math, science에 대한 점수를 기록할 수 있고, 어떤 학생이 언제 본 시험인지도 기록해주세요.

class Score(models.Model):
    english = models.PositiveSmallIntegerField()
    math = models.PositiveSmallIntegerField()
    science = models.PositiveSmallIntegerField()
    student = models.ForeignKey("Students", on_delete=models.CASCADE)
    
    exam_date = models.DateTimeField(null=True)
    