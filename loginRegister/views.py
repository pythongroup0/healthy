from django.shortcuts import render,redirect,render_to_response
from loginRegister.models import UserInfo
from manages.models import AdminInfo
from manages import views
from .apps import UserRegisterForm,UserLoginForm,AdminLoginForm

def userLogin(request):
    # 返回的错误信息
    error_msg = ''
    form = UserLoginForm()
    if request.method == 'POST':
        # 从表单填充数据
        form.setPost(request.POST)
        # 查询数据库
        users = UserInfo.objects.filter(username=form.username,password=form.password)
        if len(users)>=1:
            request.session['user_id'] = users[0].id
            return redirect(views.userManage)
        else:
            error_msg = '用户名或密码错误'
    return render(request,'userLogin.html',{'form':form,'error_msg':error_msg})

def userWithDraw(request):
    del request.session['user_id']
    return render(request, 'userLogin.html')

def adminLogin(request):
    error_msg = ''
    adminer=''
    form=AdminLoginForm()
    if request.method == 'POST':
        # 从表单填充数据
        form.setPost(request.POST)
        # 查询数据库
        admins = AdminInfo.objects.filter(adminname=form.adminname,password=form.password)
        if len(admins)>=1:
            request.session['admin_id'] = admins[0].id
            return redirect(views.administerManage)
        else:
            error_msg = '用户名或密码错误'
    return render(request,'adminLogin.html',{'form':form,'error_msg':error_msg})

def adminWithDraw(request):
    del request.session['admin_id']
    return render(request, 'adminLogin.html')

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
                user.setBatchAttr(form.username,form.password,form.email,form.sex,form.height,form.weight
                              ,form.age,form.allergic_food,form.taste)
                user.save()
                return redirect(userLogin)
    return render(request, 'register.html', {'form':form,'error_msg':error_msg})


