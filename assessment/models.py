from django.db import models
from enrollment.models import Enrollment

class Assessment(models.Model):
    ASSESSMENT_TYPE_CHOICES = (
        ('assignment', 'Assignment'),
        ('quiz', 'Quiz'),
        ('midterm', 'Midterm'),
        ('final', 'Final Exam'),
    )

    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(max_length=100)
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPE_CHOICES)
    marks_obtained = models.FloatField()
    max_marks = models.FloatField()
    date = models.DateField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.enrollment.student.user.username} - {self.title} ({self.assessment_type})"
