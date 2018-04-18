from django.conf.urls import url
from loginRegister.views import *

urlpatterns = [

    url('^$',index),
    url('^userlogin$',userLogin),
    url('^adminlogin$',adminLogin),
    url('^adminLogin_check$',adminLogin_check),
    url('^register$',register)
]