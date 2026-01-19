from rest_framework import serializers
from .models import StudentProfile, TeacherProfile
from academics.serializers import DepartmentSerializer, CoursesSerializer
from academics.models import Department


class StudentProfileSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    courses = CoursesSerializer(many=True, read_only=True)

    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        write_only=True,
        source='department'
    )

    class Meta:
        model = StudentProfile
        fields = [
            'registration_number',
            'department', 'department_id',
            'semester',
            'courses',
            'date_of_birth',
            'phone_number',
            'profile_picture',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return StudentProfile.objects.create(user=user, **validated_data)

class TeacherProfileSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    assigned_courses = CoursesSerializer(many=True, read_only=True)
    employee_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = TeacherProfile
        fields = ['employee_id', 'department', 'assigned_courses',
                  'phone_number', 'profile_picture','date_of_joining']

    def create(self, validated_data):
        user = self.context['request'].user
        return TeacherProfile.objects.create(user=user, **validated_data)