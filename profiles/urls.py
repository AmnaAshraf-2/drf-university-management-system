from django.urls import path
from .views import StudentProfileView, TeacherProfileView, AssignTeacherView, AssignStudentView

urlpatterns = [
    path('sdashboard/', StudentProfileView.as_view()),
    path('tdashboard/', TeacherProfileView.as_view()),
    path('assign-teacher/<int:pk>/', AssignTeacherView.as_view(), name='assign-teacher'),
    path('assign-student/<int:pk>/', AssignStudentView.as_view(), name='assign-student'),
]