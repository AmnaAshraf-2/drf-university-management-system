from portal.serializers import UserSerializer
from .permissions import IsStudent,IsTeacher
from .serializers import StudentProfileSerializer, TeacherProfileSerializer
from .models import StudentProfile, TeacherProfile
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from academics.models import Department

# from academics.setializers import DepartmentSerializer


class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentProfileSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsStudent]

    def get_object(self):
        user = self.request.user
        profile, created = StudentProfile.objects.get_or_create(
            user=user,
            defaults={
                'department': Department.objects.first(),
                'registration_number': f"STU-{user.id:06d}"
            }
        )
        return profile

    def retrieve(self, request, *args, **kwargs):

        profile = self.get_object()
        profile_data = self.get_serializer(profile).data
        user_data = UserSerializer(request.user).data

        return Response({
            'message': 'Welcome to the student dashboard!',
            'user': user_data,
            'profile': profile_data
        })


class TeacherProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = TeacherProfileSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_object(self):
        user = self.request.user

        profile, created = TeacherProfile.objects.get_or_create(
            user=user,
            defaults={
                'employee_id': f"TEA-{user.id:06d}",
                'department': None
            }
        )
        return profile

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        profile_data = self.get_serializer(profile).data
        user_data = UserSerializer(request.user).data

        return Response({
            'message': 'Welcome to the teacher dashboard!',
            'user': user_data,
            'profile': profile_data
        })

class DepartmentAssignmentUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        pass