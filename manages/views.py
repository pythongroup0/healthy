from django.shortcuts import render,redirect
from loginRegister.models import UserInfo
from loginRegister.apps import UserRegisterForm

def administerManage(request):
    user_list=UserInfo.objects.all()
    return render(request,'administerManage.html',{'user_list':user_list})

def adminDeleteUser(request,id):
    UserInfo.objects.filter(id=id).delete()
    user_list = UserInfo.objects.all()
    return render(request, 'administerManage.html', {'user_list': user_list})
def adminAddUser(request):
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
                user.setBatchAttr(form.username, form.password, form.email, form.sex, form.height, form.weight
                                  , form.age, form.allergic_food, form.taste)
                user.save()
                return redirect(administerManage)
    return render(request, 'administerManage.html', { 'error_msg': error_msg})
def adminChangeUser(request,id):
    error_msg = ''
    form = UserRegisterForm()
    if request.method == 'POST':
        try:
            form.setPost(request.POST)
        except Exception:
            error_msg = '数据格式不正确'
        else:
            Query_user = UserInfo.objects.filter(username=form.username)
            if len(Query_user) >= 2:
                error_msg = '用户名已存在'
            else:
                UserInfo.objects.filter(id=id).update(username=form.username,password=form.password,
                email=form.email,gender=form.sex,height=form.height,weight=form.weight,age=form.age,
                                                      senstive=form.allergic_food,perfer=form.taste)
        return redirect(administerManage)
    return render(request, 'administerManage.html', {'error_msg': error_msg})

def adminSearchUser(request):
    error_msg = ''
    if request.method == 'POST':
        researchUser = request.POST['searchUser']
        print(researchUser)
        if researchUser=="":
            error_msg='请输入用户名搜索'
            user_list =UserInfo.objects.all()
            return render(request, 'administerManage.html', {'user_list': user_list,'error_msg':error_msg})
        else:
            username = UserInfo.objects.filter(username__contains=researchUser)
            print(username)
            if len(username)>=1:
                user_list=UserInfo.objects.filter(username__contains=researchUser)
                print(user_list)
                return render(request, 'administerManage.html', {'user_list': user_list})
            else:
                error_msg='不存在该用户'
    return render(request, 'administerManage.html', {'error_msg': error_msg})
def display(request):
    context = {}
    return render(request, 'display.html', context)
def userManage(request):
    context = {}
    return render(request, 'userManage.html', context)
