from django.urls import path
from account.views import _logout, change_password, profile_edit, user_enrolled
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login',auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name='login'),
    path('logout', _logout, name='logout'),
    path('change-password', change_password, name='change-password'),
    path('profile-edit', profile_edit, name='profile-edit'),
    path('register', user_enrolled, name='register')
]
