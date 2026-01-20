from rest_framework import serializers
from .models import StudentProfile, TeacherProfile
from academics.serializers import DepartmentSerializer, CoursesSerializer
from academics.models import Department,Courses


class StudentProfileSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    courses = CoursesSerializer(many=True, read_only=True)
    registration_number = serializers.CharField(read_only=True)
    semester = serializers.CharField(read_only=True)
    date_of_birth = serializers.DateField(read_only=True)

    class Meta:
        model = StudentProfile
        fields = [
            'registration_number',
            'department',
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
    employee_id = serializers.PrimaryKeyRelatedField(read_only=True)
    date_of_joining = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TeacherProfile
        fields = [
            'employee_id',
            'department',
            'assigned_courses',
            'phone_number',
            'profile_picture',
            'date_of_joining'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return TeacherProfile.objects.create(user=user, **validated_data)

class TeacherAssignmentSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    assigned_courses = serializers.PrimaryKeyRelatedField(
        queryset=Courses.objects.all(),
        many=True
    )

    class Meta:
        model = TeacherProfile
        fields = ['department', 'assigned_courses']


class StudentAssignmentSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    enrolled_courses = serializers.PrimaryKeyRelatedField(
        queryset=Courses.objects.all(),
        many=True
    )

    class Meta:
        model = StudentProfile
        fields = ['department', 'courses']