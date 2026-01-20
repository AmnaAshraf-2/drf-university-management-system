from rest_framework import serializers
from .models import Courses, Department

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'code', 'tittle']

class DepartmentSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True, read_only=True)  # reverse relation

    class Meta:
        model = Department
        fields = ['id', 'name', 'courses']