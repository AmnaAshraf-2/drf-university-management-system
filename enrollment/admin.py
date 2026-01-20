from django.contrib import admin
from .models import Enrollment

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'enrollment_date', 'grade')
    list_filter = ('status', 'course')
    search_fields = ('student__user__username', 'course__tittle')

admin.site.register(Enrollment, EnrollmentAdmin)
