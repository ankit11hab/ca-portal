from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import VerificationView

urlpatterns = [
    path('register-single/', user_views.register_single_user, name='register_single'),
    path('register-group/', user_views.register_group_user, name='register_group'),
    path('login/', user_views.loginPage, name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('scoring_system/',user_views.scoring,name='scoring'),
    path('guidelines/',user_views.guidelines,name='guidelines'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/landing_page.html'), name='logout'),
    # Password reset urls
    path("password_reset", user_views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/password_reset_complete.html'), name='password_reset_complete'),
]

