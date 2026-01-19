from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', RegisterAPIView.as_view(), name='auth_register'),
    path('login/', LoginAPIView.as_view(), name='auth_login'),
]