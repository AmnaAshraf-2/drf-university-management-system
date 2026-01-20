from django.contrib import admin
from .models import Assessment

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'title', 'assessment_type', 'marks_obtained', 'max_marks', 'date')
    list_filter = ('assessment_type', 'date', 'enrollment__course')
    search_fields = ('enrollment__student__user__username', 'title')

admin.site.register(Assessment, AssessmentAdmin)
