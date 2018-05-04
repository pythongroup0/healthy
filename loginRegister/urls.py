from django.conf.urls import url
from loginRegister.views import *

urlpatterns = [

    url('^$',userLogin),
    url('^userLogin$',userLogin),
    url('^adminLogin$',adminLogin),
    url('^register$',register)
]