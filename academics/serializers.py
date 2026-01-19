from rest_framework import serializers
from .models import Courses, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['tittle', 'department', 'code']