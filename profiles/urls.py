from django.urls import path
from .views import StudentProfileView, TeacherProfileView, TeachersView, StudentsView

urlpatterns = [
    path('sdashboard/', StudentProfileView.as_view()),
    path('tdashboard/', TeacherProfileView.as_view()),
    path('teachers/', TeachersView.as_view()),
    path('students/', StudentsView.as_view()),
]