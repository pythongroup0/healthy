from django.conf.urls import url
from manages.views import *

urlpatterns = [
    url('^administermanage$',administerManage),
    #管理员对于用户的增删改查
    url('^adminDeleteUser/(\d+)$',adminDeleteUser),
    url('^adminAddUser$',adminAddUser),
    url('^adminChangeUser/(\d+)$',adminChangeUser),
    url('^adminSearchUser$',adminSearchUser),

    url('^userManage/$',userManage),
    url('^I_changeUser/(\d+)', I_changeUser),
    url('^display$',display),

    #管理员对于菜品的增删改查
    url('^adminAddDish$',adminAddDish),
    url('^adminDeleteDish/(\d+)$',adminDeleteDish),
    url('^adminChangeDish/(\d+)$',adminChangeDish),
    url('^adminSearchDish$', adminSearchDish),

    #管理员对于食材的增删改查
    url('^adminAddIngredients$', adminAddIngredients),
    url('^adminDeleteIngredients/(\d+)$', adminDeleteIngredients),
    url('^adminChangeIngredients/(\d+)$', adminChangeIngredients),
    url('^adminSearchIngredients$', adminSearchIngredients),

]