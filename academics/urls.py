from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CoursesViewSet, DepartmentViewSet

router = SimpleRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'departments', DepartmentViewSet, basename='departments')
urlpatterns = [
    path('', include(router.urls))
]
