from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from django.http import QueryDict
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User= get_user_model()

# Create your views here.
class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        login= request.data.get('login')
        if not login:
            return Response({"detail":"login is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data[User.USERNAME_FIELD] = request.data["login"]
        return super().post(request, *args, **kwargs)
    
class Logout(APIView):
    authentication_classes= []
    permission_classes= []

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"detail":"refresh_token is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"detail": "log out request not successful"}, status=status.HTTP_400_BAD_REQUEST)