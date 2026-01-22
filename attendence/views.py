from profiles.permissions import IsTeacher, IsStudent
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceCreateSerializer, AttendanceReadSerializer


class MarkAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceCreateSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class MyAttendanceView(generics.ListAPIView):
    serializer_class = AttendanceReadSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def get_queryset(self):
        return Attendance.objects.filter(
            enrollment__student__user=self.request.user
        ).select_related('enrollment__course')
