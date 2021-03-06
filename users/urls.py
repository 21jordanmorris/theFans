from django.urls import path, include
from .views import UserRegistrationView, SignUpView, UserUpdateView, UserPasswordChangeView, UserPasswordResetView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('<slug>/update/', UserUpdateView.as_view(), name='update_user'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]