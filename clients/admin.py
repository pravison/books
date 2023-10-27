from django.contrib import admin
from .models import Client, Newsletter, Contact_us_Message, Domain
# Register your models here.
admin.site.register(Client)
admin.register(Domain)
admin.site.register(Newsletter)
admin.site.register(Contact_us_Message)
