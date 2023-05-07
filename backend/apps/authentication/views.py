from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, status, decorators
from rest_framework.response import Response
from django.http import QueryDict
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from apps.utils.helpers.commons import Utils 

UserModel= get_user_model()  

class AuthViewSet(TokenObtainPairView, viewsets.ModelViewSet):
    queryset= UserModel.objects
    authentication_classes= []
    permission_classes= []

    @decorators.action(detail=False, methods=["post"])
    def login(self, request, *args, **kwargs):
        login= request.data.get('login')
        if not login:
            return Response({"detail":"login is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data[UserModel.USERNAME_FIELD] = request.data["login"]
        return super().post(request, *args, **kwargs)

    @decorators.action(detail=False, methods=["post"])
    def logout(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
           return Utils.error_response("refresh_token is required", ["no refresh token"], status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Utils.success_response({"detail": "logged out successfully"}, status.HTTP_200_OK)
        except Exception as err:
            return Utils.error_response("log out request not successful", ["token error"], status.HTTP_400_BAD_REQUEST)

    @decorators.action(detail=False, methods=["post"])
    def initiate_reset_password_email(self, request, *args, **kwargs):
        email= request.data.get("email")
        instance= Utils.get_object_or_raise_error(UserModel, email=email)

    @decorators.action(detail=False, methods=["post"])
    def finalize_reset_password_email(self, request, *args, **kwargs):
        pass

    @decorators.action(detail=False, methods=["post"])
    def initiate_reset_password_phone(self, request, *args, **kwargs):
        pass

    @decorators.action(detail=False, methods=["post"])
    def finalize_reset_password_phone(self, request, *args, **kwargs):
        pass