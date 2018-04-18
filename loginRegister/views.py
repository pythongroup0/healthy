from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from loginRegister.models import UserInfo
from manages import views

class UserLoginForm():
    def __init__(self,username='',password=''):
        self.username = username
        self.password = password
    def setPost(self,post):
        self.username = post['username']
        self.password = post['password']

class UserRegisterForm():
    username = ''
    password = ''
    sex = True
    height = 0
    weight = 0
    age = 0
    allergic_food = ''
    taste = ''

    def setPost(self,post):
        self.username = post['username']
        self.password = post['password']
        self.sex = bool(post['sex'])
        self.height = float(post['height'])
        self.weight = float(post['weight'])
        self.age = float(post['age'])
        self.allergic_food = post['allergic_food']
        self.taste = post['taste']


def userLogin(request):
    # 返回的错误信息
    error_msg = ''
    form = UserLoginForm()
    if request.method == 'POST':
        # 从表单填充数据
        form.setPost(request.POST)
        # 查询数据库
        user = UserInfo.objects.filter(username=form.username,password=form.password)
        if len(user)>=1:
            return redirect(views.userManage)
        else:
            error_msg = '用户名或密码错误'
    return render(request,'userLogin.html',{'form':form,'error_msg':error_msg})

def adminLogin(request):
    context = {}
    return render(request,'adminLogin.html',context)

def register(request):
    error_msg = ''
    form = UserRegisterForm()
    if request.method == 'POST':
        try:
            form.setPost(request.POST)
        except Exception:
            error_msg = '数据格式不正确'
        else:
            Query_user = UserInfo.objects.filter(username=form.username)
            if len(Query_user) >= 1:
                error_msg = '用户名已存在'
            else:
                user = UserInfo()
                user.setBatchAttr(form.username,form.password,form.sex,form.height,form.weight
                              ,form.age,form.allergic_food,form.taste)
                user.save()
                return redirect(userLogin)
    return render(request, 'register.html', {'form':form,'error_msg':error_msg})


