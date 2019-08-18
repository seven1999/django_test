from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserTab, ShopTab


class UserTabAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_mobile', 'user_idno',)


class ShopTabAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(UserTab, UserTabAdmin)
admin.site.register(ShopTab, ShopTabAdmin)

