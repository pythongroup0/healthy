from django.conf.urls import url
from manages.views import *

urlpatterns = [
    url('^administermanage$',administerManage),
    url('^usermanage$',userManage),
    # 用户增删改查网址
    url('^adminAddUser$',adminAddUser),
    url('^adminDeleteUser/(\d+)$',adminDeleteUser),
    url('^adminChangeUser/(\d+)$',adminChangeUser),
    url('^adminSearchUser$',adminSearchUser),

    #食材增删改查网址
    url('^adminAddIngredients$',adminAddIngredients),
    url('^adminDeleteIngredients/(\d+)$',adminDeleteIngredients),
    url('^adminChangeIngredients/(\d+)$',adminChangeIngredients),
    url('^adminSearchIngredients$',adminSearchIngredients),


    url('^display$',display),
]