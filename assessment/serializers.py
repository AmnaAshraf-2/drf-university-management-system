from rest_framework import serializers
from .models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='enrollment.student.user.username', read_only=True)
    course_title = serializers.CharField(source='enrollment.course.tittle', read_only=True)

    class Meta:
        model = Assessment
        fields = ['id', 'enrollment', 'student_name', 'course_title', 'assessment_type', 'marks_obtained', 'max_marks', 'date', 'remarks']
