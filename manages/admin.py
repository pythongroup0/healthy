from django.contrib import admin
from manages.models import AdminInfo,AdminInfoAdmin,DishInfo,DishInfoAdmin,IngredientsInfo,IngredientsInfoAdmin
# Register your models here.
admin.site.register(AdminInfo,AdminInfoAdmin)
admin.site.register(DishInfo,DishInfoAdmin)
admin.site.register(IngredientsInfo,IngredientsInfoAdmin)