from profiles.permissions import IsTeacher
from rest_framework import generics
from .models import Assessment
from .serializers import AssessmentSerializer
from enrollment.models import Enrollment
from rest_framework.exceptions import PermissionDenied


class TeacherAssessmentView(generics.ListCreateAPIView):
    permission_classes = [IsTeacher]
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        teacher = self.request.user.teacher_profile
        return Assessment.objects.filter(
            enrollment__course__in=teacher.assigned_courses.all()
        )

    def perform_create(self, serializer):
        teacher = self.request.user.teacher_profile
        enrollment = serializer.validated_data['enrollment']

        if enrollment.course not in teacher.assigned_courses.all():
            raise PermissionDenied("You cannot mark assessment for this course")

        serializer.save()