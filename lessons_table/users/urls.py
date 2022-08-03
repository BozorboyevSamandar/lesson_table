from django.urls import path
from .views import RegisterUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

urlpatterns = [
    path('register', RegisterUserViewSet.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
]
