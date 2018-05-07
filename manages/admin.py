from django.contrib import admin
from manages.models import *

# Register your models here.
admin.site.register(AdminInfo,AdminInfoAdmin)
admin.site.register(DishInfo,DishInfoAdmin)
admin.site.register(IngredientsInfo,IngredientsInfoAdmin)
admin.site.register(DishAndIngredient,DishIngredientsAdmin)
