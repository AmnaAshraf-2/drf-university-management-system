from django.db import models
from portal.models import User
from academics.models import Department, Courses
from django.db.models.signals import post_save
from django.dispatch import receiver


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    registration_number = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField(default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Student"


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    assigned_courses = models.ManyToManyField(Courses, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Teacher"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    department = Department.objects.first()
    if not department:
        return

    if instance.role == 'student':
        StudentProfile.objects.create(
            user=instance,
            department=department,
            registration_number=f"STU-{instance.id:06d}"
        )

    elif instance.role == 'teacher':
        TeacherProfile.objects.create(
            user=instance,
            department=department,
            employee_id=f"EMP-{instance.id:06d}"
        )
