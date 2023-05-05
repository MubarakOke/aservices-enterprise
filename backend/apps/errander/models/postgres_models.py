from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.utils.helpers.models import BaseUserModelMixin, BaseModelBaseMixin
from apps.utils.enums.errander import (GenderType, EducationType, InternetType)

# storrage location for images
def errander_image_location(instance, filename):
    return f"Aservices/Errander/{instance.user.email}/photo/{filename}"

def customer_image_location(instance, filename):
    return f"Aservices/Customer/{instance.user.email}/photo/{filename}"

# model picture property
def pictureURL(self):
        if self.picture:
            return self.picture.url
        return None

# worker model
class Worker(BaseUserModelMixin):
    user= user = models.OneToOneField(
        'authentication.User',
        on_delete=models.CASCADE,
        null=False,
        related_name="worker",
        verbose_name=_("Errander Workers"),
    )
    address= models.CharField(_("Worker Address"), max_length=150, blank=False, null=True)
    lga= models.CharField(_("Worker LGA"), max_length=150, blank=False, null=True)
    city = models.CharField(_("Worker city"), max_length=150, blank=False, null=True)
    gender= models.CharField(_("Worker gender"), max_length=50, blank=False, null=True, choices=GenderType.choices())
    date_of_birth= models.DateField(_("Worker date of birth"), blank=False, null=True)
    education_qualification= models.CharField(_("Worker education stage"), max_length=150, blank=False, null=True, choices=EducationType.choices())
    internet_usage= models.CharField(_("Worker internet usage experience"), max_length=50, blank=False, null=True, choices=InternetType.choices())
    skill= models.TextField(_("Worker skillset"), blank=False, null=True)
    deadline_handling= models.TextField(_("Deadline Management"), blank=False, null=True)
    project= models.TextField(_("Numbers of project handled"), blank=False, null=True)
    expectation= models.TextField(_("expectation from the company"), blank=False, null=True)
    relevant_information=models.TextField(_("Information that is helpful"), blank=False, null=True)
    interest= models.TextField(_("Errander interest"), blank=False, null=True)
    familiar_location=models.TextField(_("Location understanding"), blank=False, null=True)
    picture= models.ImageField(upload_to=errander_image_location, blank=True, null=True)
    is_verified= models.BooleanField(_("Worker verification status"), default=False)
    is_declined= models.BooleanField(_("Worker Declination status"), default=False)
    active= models.BooleanField(default=False)
    pictureURL= property(pictureURL)

    class Meta:
        verbose_name = _("Worker Profile")
        verbose_name_plural = _("Worker Profile")

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"
        
    
# customer model
class Customer(BaseUserModelMixin):
    user= models.OneToOneField('authentication.User', 
                               blank=True, 
                               on_delete= models.CASCADE, 
                               related_name="customer", 
                               verbose_name="Errander Customer",
                                )  
    picture= models.ImageField(upload_to=customer_image_location, blank=True, null=True)
    is_verified= models.BooleanField(_("Worker verification status"), default=False)
    pictureURL= property(pictureURL)

    class Meta:
        verbose_name = _("Customer Profile")
        verbose_name_plural = _("Customer Profile")
    
    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

# order model
class Order(BaseModelBaseMixin, models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name="order")
    errander= models.ForeignKey(Worker, on_delete=models.SET_NULL, blank=True, null=True, related_name='order')
    date_created= models.DateField(auto_now_add=True)
    date_completed= models.DateField(auto_now=True)
    status= models.CharField(_("Order status"), max_length=50, blank=True, null=True)
    address= models.CharField(_("Delivery Address"), max_length=150, blank=True, null=True)
    relevant_detail= models.TextField(_("Address relevant info"), blank=True, null=True)
    preferred_shop= models.CharField(_("Shop to purchase item"), max_length=150, blank=True, null=True)
    preferred_shop_location= models.CharField(_("Location of shop of choice"), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order {self.id}-{self.customer.user.first_name}"
    

# Stock model
class Stock(models.Model): 
    name= models.CharField(_("Order name"), max_length=255, blank=True, null=True)
    quantity= models.IntegerField(_("Order quantity"), blank=True, null=True)
    price= models.FloatField(_("Order price"), blank=True, null=True)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name='stock', verbose_name="Order stock")
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name="stock", verbose_name="Customer stock")

    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")

    def __str__(self):
        return f"Order {self.order.id}-{self.name}-{self.price}"