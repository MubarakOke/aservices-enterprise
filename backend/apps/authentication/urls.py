from django.urls import path, re_path, include
from .literals import (APP_NAME, LOGIN_VIEW_NAME, LOGOUT_VIEW_NAME)
from . import views 


app_name= APP_NAME

urlpatterns = [
    path("login", views.Login.as_view(), name=LOGIN_VIEW_NAME),
    path("logout", views.Logout.as_view(), name=LOGOUT_VIEW_NAME)
]
