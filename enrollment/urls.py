from django.urls import path
from .views import (
    EnrollmentCreateView,
    EnrollmentListView,
    StudentEnrollmentsView,
    TeacherAssignmentView,
)


urlpatterns = [
    path('enrollments/', EnrollmentListView.as_view()),
    path('enrollments/assign/', EnrollmentCreateView.as_view()),
    path('enrollments/student/', StudentEnrollmentsView.as_view()),
    path('at/<int:pk>/', TeacherAssignmentView.as_view()),
]