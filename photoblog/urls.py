"""
URL configuration for photoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import blog.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name = 'authentication/login.html',
        redirect_authenticated_user = True
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(template_name='authentication/password_change_form.html'), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
    path('home/', blog.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
]