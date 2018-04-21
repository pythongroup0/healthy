from django.test import TestCase
from loginRegister.models import UserInfo

# Create your tests here.
user_list=UserInfo.objects.filter(username='ruthy')
print(user_list)