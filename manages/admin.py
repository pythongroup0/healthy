from django.contrib import admin
from manages.models import AdminInfo,AdminInfoAdmin
# Register your models here.
admin.site.register(AdminInfo,AdminInfoAdmin)