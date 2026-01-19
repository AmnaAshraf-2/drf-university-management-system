from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username','first_name','last_name', 'email', 'role','is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('id',)

admin.site.register(User, UserAdmin)
