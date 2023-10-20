from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.StudentView.as_view()),
    path('students/<int:pk>', views.StudentDetailView.as_view()),
    path('score/', views.ScoreView),
    path('score/<int:pk>', views.ScoreDetailView),
    path('students/<int:pk>/score', views.StudentScoreView)
    
    
]
