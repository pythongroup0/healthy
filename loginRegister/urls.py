from django.conf.urls import url
from loginRegister.views import *

urlpatterns = [
    url('^userlogin$',userLogin),
    url('^adminlogin$',adminLogin),
    url('^register$',register)
]