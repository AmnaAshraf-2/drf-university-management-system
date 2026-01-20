from django.urls import path
from .views import TeacherAssessmentView

urlpatterns = [
    path('assessment/', TeacherAssessmentView.as_view()),
]