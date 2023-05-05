from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.utils.enums.authentication import  UserType
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, phone, password, **extra_fields):      
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email= self.normalize_email(email),
            phone= phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, phone, password, **extra_fields):
        return self._create_user(email, password, phone, **extra_fields)
    
    def create_superuser(self, email, phone, password, **extra_fields):
        extra_fields.setdefault("user_type", UserType.SUPERADMIN.value)
        return self._create_user(email, phone, password, **extra_fields)
    
    def get_by_phone_number(self, phone_number):
        return self.get(**{"phone": phone_number})

# user model
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_email_verified = models.BooleanField(_("Email Verified?"), default=False, blank=True, null=False)
    phone= models.CharField(_("Phone Number"), max_length=50, null=False, blank=False, unique=True)
    is_phone_number_verified = models.BooleanField(_("Phone Number Verified?"), default=False, blank=True, null=False)
    user_type = models.CharField(_("User Type"),
        choices=UserType.choices(),
        default=UserType.USER.value,
        null=False,
        blank=False,
        max_length=20,
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def is_staff(self):
        return self.user_type==UserType.SUPERADMIN.value
