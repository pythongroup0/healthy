from django.conf.urls import url
from manages.views import *

urlpatterns = [
    url('^administermanage$',administerManage),
    url('^usermanage$',userManage),
    url('^display$',display),
]