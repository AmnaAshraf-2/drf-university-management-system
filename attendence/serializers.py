from rest_framework import serializers
from .models import Attendance


class AttendanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['enrollment', 'date', 'status']

    def validate_enrollment(self, enrollment):
        request = self.context['request']
        teacher = getattr(request.user, 'teacherprofile', None)

        if not teacher:
            raise serializers.ValidationError("Only teachers can mark attendance.")

        if enrollment.course not in teacher.assigned_courses.all():
            raise serializers.ValidationError(
                "You are not assigned to this course."
            )

        return enrollment


class AttendanceReadSerializer(serializers.ModelSerializer):
    course = serializers.CharField(
        source='enrollment.course.tittle',
        read_only=True
    )
    date = serializers.DateField()
    status = serializers.CharField()

    class Meta:
        model = Attendance
        fields = ['course', 'date', 'status']
