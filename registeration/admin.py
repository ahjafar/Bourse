from django.contrib import admin
from .models import Temp_user,Password_reset
# Register your models here.




@admin.register(Temp_user)
class Temp_UserAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Temp_user._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)


@admin.register(Password_reset)
class Password_ResatAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Password_reset._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)

# admin.site.register(Temp_user)
# admin.site.register(Password_reset)
