from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (
    logout_view,
    home_view,
)

app_name = 'staff'

urlpatterns = [
    path('', home_view, name='home'),
    path(
        'login/',
        LoginView.as_view(
            template_name='staff/login.html',
            redirect_authenticated_user=True,
        ),
        name='login'
    ),
    path('accounts/logout/', logout_view, name='logout'),
]