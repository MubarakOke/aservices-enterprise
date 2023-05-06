from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModelBaseMixin:
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True,)
    timestamp = models.DateTimeField(_("update time"), auto_now=True,)

    def is_instance_exist(self):
        return self.__class__.objects.filter(id=self.id).exists()

    @property
    def current_instance(self):
        return self.__class__.objects.get(id=self.id)

    @classmethod
    def efficient_queryset_iterator(cls, chunk_size=10):
        pass

class BaseUserModelMixin(BaseModelBaseMixin, models.Model):
    first_name= models.CharField(max_length=255, blank=False, null=True)
    last_name= models.CharField(max_length=255, blank=False, null=True)
    middle_name= models.CharField(max_length=255, blank=False, null=True)
    phone= models.CharField(max_length=15, blank=False, null=True)
    user_type= models.CharField(max_length=255, blank=False, null=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
    
    def sent_otp(self, channel="email"):
        pass

    def verify_otp(self):
        pass

    def send_email(self):
        pass
