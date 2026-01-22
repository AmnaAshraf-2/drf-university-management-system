from django.db.models.signals import post_save
from django.dispatch import receiver
from portal.models import User
from academics.models import Department
from .models import StudentProfile, TeacherProfile


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
