from django.db import models
from academics.models import Courses
from profiles.models import StudentProfile


class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    )
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='enrolled')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = (('course', 'student'),)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.tittle}"

