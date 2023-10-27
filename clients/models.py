from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200, unique=True)
    paid_until = models.DateField(blank=True, null=True)
    on_trial = models.BooleanField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    refferal_code = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    #schema will be automatically created and synced when saved
    auto_create_schema= True
    auto_drop_schema = True


    def __str__(self):
        return str(self.name)

class Domain(DomainMixin):
    pass

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact_us_Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name