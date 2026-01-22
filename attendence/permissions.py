from rest_framework.permissions import BasePermission

class IsAssignedCourseTeacher(BasePermission):
    message = "You are not assigned to this course."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        teacher_profile = getattr(request.user, 'teacherprofile', None)
        if not teacher_profile:
            return False

        return obj.course in teacher_profile.assigned_courses.all()
