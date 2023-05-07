from django.urls import path, re_path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from .literals import (APP_NAME, BASE_NAME, LOGIN_VIEW_NAME, LOGOUT_VIEW_NAME)
from . import views 

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name= APP_NAME
router.register("", views.AuthViewSet, basename=BASE_NAME)

urlpatterns= router.urls
# urlpatterns = [
#     path("login", views.Login.as_view(), name=LOGIN_VIEW_NAME),
#     path("logout", views.Logout.as_view(), name=LOGOUT_VIEW_NAME)
# ]
