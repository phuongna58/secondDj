from django.urls import path
from .views import UserLoginView, UserRegisterView

urlpatterns = [
    path('api/login/', UserLoginView.as_view(), name='user_login'),
    path('api/register', UserRegisterView.as_view(), name='user_register')
]
