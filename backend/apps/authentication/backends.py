from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel= get_user_model()
      
class PhoneNumberAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        login = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_phone_number(login)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
