from rest_framework import serializers
from .models import Enrollment
from academics.models import Courses, Department
from profiles.models import StudentProfile, TeacherProfile


class EnrollmentReadSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username', read_only=True)
    course = serializers.CharField(source='course.tittle', read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'student',
            'course',
            'semester',
            'status',
            'grade',
            'enrollment_date',
        ]


class EnrollmentCreateSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all()
    )
    courses = serializers.PrimaryKeyRelatedField(
        queryset=Courses.objects.all(),
        many=True
    )
    semester = serializers.CharField(max_length=10)

    def create(self, validated_data):
        student = validated_data['student']
        semester = validated_data['semester']
        courses = validated_data['courses']

        already_enrolled = Enrollment.objects.filter(
            student=student,
            course__in=courses
        ).values_list('course_id', flat=True)

        new_courses = [c for c in courses if c.id not in already_enrolled]

        if not new_courses:
            raise serializers.ValidationError(
                "Student is already enrolled in all selected courses."
            )

        enrollments = [
            Enrollment(student=student, course=course, semester=semester)
            for course in new_courses
        ]

        Enrollment.objects.bulk_create(enrollments)
        return enrollments


class StudentInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'full_name', 'email']

    def get_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else None


class StudentEnrollmentSummarySerializer(serializers.ModelSerializer):
    student_info = StudentInfoSerializer(source='*', read_only=True)
    department = serializers.StringRelatedField(read_only=True)
    enrolled_courses = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = [
            'student_info',
            'department',
            'enrolled_courses',
        ]

    def get_enrolled_courses(self, obj):
        return [
            enrollment.course.tittle
            for enrollment in obj.enrollment_set.all()
        ]


class StudentAssignmentWriteSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    courses = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all(), many=True, required=False)

    class Meta:
        model = StudentProfile
        fields = ['department', 'courses']

    def update(self, instance, validated_data):
        instance.department = validated_data.get('department', instance.department)
        instance.save()

        if 'courses' in validated_data:
            instance.courses.set(validated_data['courses'])

        return instance


class TeacherInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ['id', 'full_name', 'email']

    def get_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else None


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    teacher_info = TeacherInfoSerializer(source='*', read_only=True)
    department = serializers.StringRelatedField(read_only=True)
    assigned_courses = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TeacherProfile
        fields = [
            'teacher_info',
            'department',
            'assigned_courses',
        ]


class TeacherAssignmentWriteSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    assigned_courses = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all(), many=True)

    class Meta:
        model = TeacherProfile
        fields = ['department', 'assigned_courses']

    def update(self, instance, validated_data):
        instance.department = validated_data.get('department', instance.department)
        instance.save()

        if 'assigned_courses' in validated_data:
            instance.assigned_courses.set(validated_data['assigned_courses'])

        return instance
