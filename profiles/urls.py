from django.urls import path
from .views import StudentProfileView, TeacherProfileView, DepartmentAssignmentUpdateAPIView

urlpatterns = [
    path('sdashboard/', StudentProfileView.as_view()),
    path('tdashboard/', TeacherProfileView.as_view()),
]