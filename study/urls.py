from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', 
                views.StudentViewSet)
router.register('score', 
                views.ScoreViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('students/', views.StudentView.as_view()),
    # path('students/<int:pk>', views.StudentDetailView.as_view()),
    # path('score/', views.ScoreView),
    # path('score/<int:pk>', views.ScoreDetailView),
    # path('students/<int:pk>/score', views.StudentScoreView)
]
