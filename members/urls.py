from django.urls import path
from .views import UserRegisterView, UserUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserUpdateView.as_view(), name='edit-profile'),

]