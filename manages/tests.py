from django.test import TestCase
from manages.models import DishInfo

# Create your tests here.
dish_list=DishInfo.objects.all()
print(dish_list)