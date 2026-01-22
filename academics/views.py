from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Department, Courses
from .serializers import DepartmentSerializer, CoursesSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset =  Courses.objects.all()
    serializer_class = CoursesSerializer
