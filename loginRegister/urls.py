from django.conf.urls import url
from loginRegister.views import *

urlpatterns = [
    url('^$',userLogin),
    url('^userLogin$',userLogin),
    url('^userlogin$', userLogin),
    url('^adminLogin$',adminLogin),
    url('^adminlogin$',adminLogin),
    url('^register$',register),
    url('^loginWithDraw',userWithDraw),
    url('^adminWithDraw',adminWithDraw),
]