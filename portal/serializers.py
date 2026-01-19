from rest_framework import serializers
from .models import User
from profiles.models import StudentProfile, TeacherProfile
from academics.models import Courses, Department


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'email', 'role')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password', 'role')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LogInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


