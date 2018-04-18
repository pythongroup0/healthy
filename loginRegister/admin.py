from django.contrib import admin
from loginRegister.models import UserInfo,UserInfoAdmin

admin.site.register(UserInfo, UserInfoAdmin)
