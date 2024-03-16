from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget_password_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('reset-password/<active_code>', ResetPasswordView.as_view(), name='reset_password_page'),
    path('active-account/<email_active_code>', ActiveAccountView.as_view(), name='active_password_page'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile_page'),
]
