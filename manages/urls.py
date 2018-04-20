from django.conf.urls import url
from manages.views import *

urlpatterns = [
    url('^administermanage$',administerManage),
    url('^adminDeleteUser/(\d+)$',adminDeleteUser),
    url('^adminAddUser$',adminAddUser),
    url('^adminChangeUser/(\d+)$',adminChangeUser),
    url('^usermanage$',userManage),
    url('^display$',display),
]