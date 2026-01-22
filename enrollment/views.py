from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Enrollment
from .serializers import (
    EnrollmentCreateSerializer,
    EnrollmentReadSerializer,
    TeacherAssignmentWriteSerializer,
    TeacherAssignmentSerializer
)
from profiles.permissions import IsStudent
from profiles.models import TeacherProfile


class EnrollmentCreateView(generics.CreateAPIView):

    serializer_class = EnrollmentCreateSerializer
    permission_classes = [IsAdminUser]
    queryset = Enrollment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        enrollments = serializer.save()
        read_serializer = EnrollmentReadSerializer(
            enrollments,
            many=True
        )

        return Response(
            read_serializer.data,
            status=status.HTTP_201_CREATED
        )


class EnrollmentListView(generics.ListAPIView):

    queryset = Enrollment.objects.select_related(
        'student__user',
        'course'
    )
    serializer_class = EnrollmentReadSerializer
    permission_classes = [IsAdminUser]


class StudentEnrollmentsView(generics.ListAPIView):

    serializer_class = EnrollmentReadSerializer
    permission_classes = [IsStudent]

    def get_queryset(self):
        return Enrollment.objects.filter(
            student__user=self.request.user
        ).select_related('course')


class TeacherAssignmentView(generics.RetrieveUpdateAPIView):

    permission_classes = [IsAdminUser]
    queryset = TeacherProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TeacherAssignmentWriteSerializer
        return TeacherAssignmentSerializer
