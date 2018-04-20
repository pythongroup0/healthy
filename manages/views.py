from django.shortcuts import render
from loginRegister.models import UserInfo

def administerManage(request):
    user_list=UserInfo.objects.all()
    return render(request,'administerManage.html',{'user_list':user_list})

def adminDeleteUser(request,id):
    print("i can reject id:"+id)
    UserInfo.objects.filter(id=id).delete()
    user_list = UserInfo.objects.all()
    return render(request, 'administerManage.html', {'user_list': user_list})



def display(request):
    context = {}
    return render(request, 'display.html', context)

def userManage(request):
    context = {}
    return render(request, 'userManage.html', context)
