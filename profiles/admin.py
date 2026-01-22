from django.contrib import admin
from .models import TeacherProfile, StudentProfile
from academics.models import Department, Courses


class TeacherCoursesInline(admin.TabularInline):
    model = TeacherProfile.assigned_courses.through
    extra = 1

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department')
    list_filter = ('department',)
    search_fields = ('user__username', 'employee_id')
    inlines = [TeacherCoursesInline]

class StudentCoursesInline(admin.TabularInline):
    model = StudentProfile.courses.through
    extra = 1

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'registration_number', 'department')
    list_filter = ('department',)
    search_fields = ('user__username', 'registration_number')
    inlines = [StudentCoursesInline]

admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)