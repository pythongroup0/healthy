from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from loginRegister.models import UserInfo
from manages import views

class UserLoginForm():
    username = ''
    password = ''
    def __init__(self,username,password):
        self.username = username
        self.password = password

def userLogin(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = UserLoginForm(username,password)
        user = UserInfo.objects.filter(username=form.username,password=form.password)
        length = len(user)
        if length>=1:
            return  redirect(views.userManage)
        else:
            error_msg = '用户名或密码错误'
    else:
        form = UserLoginForm('','')
    return render(request,'userLogin.html',{'form':form,'error_msg':error_msg})

def adminLogin(request):
    context = {}
    return render(request,'adminLogin.html',context)

def register(request):
    context = {}
    return render(request, 'register.html', context)


