from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='enrollment.student.user.username', read_only=True)
    course_title = serializers.CharField(source='enrollment.course.tittle', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'enrollment', 'name', 'tittle', 'date', 'status']
