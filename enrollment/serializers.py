from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.username', read_only=True)
    course_title = serializers.CharField(source='course.tittle', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'name', 'course', 'tittle', 'status', 'grade', 'enrollment_date']
