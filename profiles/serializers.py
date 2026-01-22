from rest_framework import serializers
from .models import StudentProfile, TeacherProfile
from academics.serializers import DepartmentSerializer, CoursesSerializer
from academics.models import Department,Courses


class StudentProfileSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name',read_only=True)
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
    department = serializers.SerializerMethodField(read_only=True)
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

    def get_department(self, obj):
        return obj.department.name if obj.department else None

    def create(self, validated_data):
        user = self.context['request'].user
        return TeacherProfile.objects.create(user=user, **validated_data)


class TeacherInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ['id', 'full_name', 'email']

    def get_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else None


class StudentInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    registration_number = serializers.CharField(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'full_name', 'email', 'registration_number']

    def get_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else None


