from django.urls import path, include
from .views import MarkAttendanceView, MyAttendanceView
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('attendence/', MyAttendanceView.as_view()),
    path('markattendence/', MarkAttendanceView.as_view()),
]