from django.shortcuts import render


def administerManage(request):
    context={}
    return render(request,'administerManage.html',context)

def display(request):
    context = {}
    return render(request, 'display.html', context)

def userManage(request):
    context = {}
    return render(request, 'userManage.html', context)
