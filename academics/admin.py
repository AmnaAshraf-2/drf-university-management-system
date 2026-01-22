from django.contrib import admin
from .models import Courses, Department


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'tittle', 'department')
    search_fields = ('code', 'tittle')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
