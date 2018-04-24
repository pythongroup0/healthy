from django.contrib import admin
from manages.models import AdminInfo,AdminInfoAdmin,IngredientsInfo,IngredientsInfoAdmin,DishInfo,DishInfoAdmin
# Register your models here.
admin.site.register(AdminInfo,AdminInfoAdmin)
admin.site.register(DishInfo,DishInfoAdmin)
admin.site.register(IngredientsInfo,IngredientsInfoAdmin)
