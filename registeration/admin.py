from django.contrib import admin
from .models import Temp_user,Password_reset
# Register your models here.

admin.site.register(Temp_user)
admin.site.register(Password_reset)
