from os import name
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("profile",views.profile,name="profile"),
    path("password_reset_form",views.password_reset,name="password_reset")
]