from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'date', 'status')
    list_filter = ('status', 'date', 'enrollment__course')
    search_fields = ('enrollment__student__user__username', 'enrollment__course__tittle')

admin.site.register(Attendance, AttendanceAdmin)
