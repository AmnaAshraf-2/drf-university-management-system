from django.urls import path
from .views import TeacherAssessmentView, StudentAssessmentView

urlpatterns = [
    path('mark-assessment/', TeacherAssessmentView.as_view()),
    path('view-assessment/', StudentAssessmentView.as_view()),
]