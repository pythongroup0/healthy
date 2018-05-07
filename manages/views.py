from django.shortcuts import render,redirect
from loginRegister.models import UserInfo
from manages.models import DishInfo,IngredientsInfo,AdminInfo
from loginRegister.apps import UserRegisterForm
from manages.apps import addDishForm,IngredientsForm
from django.http import HttpResponse
from django.core.paginator import Paginator
import json

#管理员管理界面

def administerManage(request):
    try:
        id = request.session['admin_id']
    except Exception:
        return render(request, 'adminLogin.html')
    flag = ''
    if request.GET.get('user_page') is None:
        user_page = 1
    else:
        user_page = int(request.GET.get('user_page'))
        flag = 'user'
    if request.GET.get('dish_page') is None:
        dish_page = 1
    else:
        dish_page = int(request.GET.get('dish_page'))
        flag = 'dish'
    if request.GET.get('ingredients_page') is None:
        ingredients_page = 1
    else:
        ingredients_page = int(request.GET.get('ingredients_page'))
        flag = 'ingredients'
    user_list=UserInfo.objects.all()
    dish_list=DishInfo.objects.all()
    ingredients_list = IngredientsInfo.objects.all()
    admin = AdminInfo.objects.get(id=id)

    user_list_pages = Paginator(user_list, 5).get_page(user_page)
    dish_list_pages = Paginator(dish_list, 3).get_page(dish_page)
    ingredients_list_pages = Paginator(ingredients_list, 3).get_page(ingredients_page)
    context = {'admin':admin,'user_list':user_list_pages,'dish_list':dish_list_pages,'ingredients_list':ingredients_list_pages
               ,'flag':flag}
    return render(request,'administerManage.html',context)


# 用户分页显示
def displayUserInfo(request):
    try:
        currentPage = int(request.GET['currentPage'])
        displayCounts = int(request.GET['displayCounts'])
    except Exception:
        return HttpResponse(json.dumps({"result":'-1'}), content_type='application/json')
    user_list = UserInfo.objects.all()
    count = len(user_list)
    if count <= 0:
        return HttpResponse(json.dumps({"result": '-2'}), content_type='application/json')

    #return HttpResponse(json.dumps(return_json), content_type='application/json')


#管理员管理用户增删改查

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

def adminDeleteUser(request,id):
    UserInfo.objects.filter(id=id).delete()
    return redirect(administerManage)

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
                dish_list = DishInfo.objects.all()
                ingredients_list = IngredientsInfo.objects.all()
                return render(request, 'administerManage.html', {'user_list': user_list,'dish_list':dish_list,'ingredients_list':ingredients_list})
            else:
                error_msg='不存在该用户'
    return render(request, 'administerManage.html', {'error_msg': error_msg})

#管理员管理菜品的增删改查

def adminAddDish(request):
    error_msg = ''
    form = addDishForm()
    if request.method == 'POST':
        try:
            form.setPost(request.POST)
        except Exception:
            error_msg = '数据格式不正确'
        else:
            Query_dish = DishInfo.objects.filter(dishName=form.dishName)
            if len(Query_dish) >= 1:
                error_msg = '菜品已存在'
            else:
                dish = DishInfo()
                dish.setBatchAttr(form.dishName, form.dishEnergy, form.dishPrice)
                dish.save()
                return redirect(administerManage)
    return render(request, 'administerManage.html', { 'error_msg': error_msg})

def adminDeleteDish(request,id):
    print('aaa')
    DishInfo.objects.filter(id=id).delete()
    return redirect(administerManage)

def adminChangeDish(request,id):
    error_msg = ''
    form = addDishForm()
    if request.method == 'POST':
        try:
            form.setPost(request.POST)
        except Exception:
            error_msg = '数据格式不正确'
        else:
            Query_dish = DishInfo.objects.filter(dishName=form.dishName)
            if len(Query_dish) >= 2:
                error_msg = '菜品已存在'
            else:
                DishInfo.objects.filter(id=id).update(dishName=form.dishName,dishEnergy=form.dishEnergy,
                dishPrice=form.dishPrice)
            return redirect(administerManage)
    return render(request, 'administerManage.html', {'error_msg': error_msg})

def adminSearchDish(request):
    error_msg = ''
    if request.method == 'POST':
        researchDish = request.POST['searchDish']
        print(researchDish)
        if researchDish=="":
            error_msg='请输入用户名搜索'
            dish_list =DishInfo.objects.all()
            return render(request, 'administerManage.html', {'dish_list': dish_list,'error_msg':error_msg})
        else:
            dishName = DishInfo.objects.filter(dishName__contains=researchDish)
            print(dishName)
            if len(dishName)>=1:
                dish_list=DishInfo.objects.filter(dishName__contains=researchDish)
                user_list = UserInfo.objects.all()
                ingredients_list = IngredientsInfo.objects.all()
                return render(request, 'administerManage.html',
                              {'user_list': user_list, 'dish_list': dish_list, 'ingredients_list': ingredients_list})
            else:
                error_msg='不存在该用户'
    return render(request, 'administerManage.html', {'error_msg': error_msg})

#管理员管理食材的增删改查
#管理员添加食材

def adminAddIngredients(request):
    error_msg = ''
    form = IngredientsForm()
    if request.method == 'POST':
        try:
            form.setPost(request.POST)
        except Exception:
            error_msg = '数据格式不正确'
        else:
            Query_ingredients = IngredientsInfo.objects.filter(ingredientsName=form.ingredientsName)
            if len(Query_ingredients) >= 1:
                error_msg = '用户名已存在'
            else:
                ingredients = IngredientsInfo()
                ingredients.setBatchAttr(form.ingredientsName, form.water, form.energy, form.protein, form.fat
                                  , form.saccharides, form.price)
                ingredients.save()
                return redirect(administerManage)
    return render(request, 'administerManage.html', {'error_msg': error_msg})
#管理员删除食材

def adminDeleteIngredients(request,id):
    IngredientsInfo.objects.filter(id=id).delete()
    return redirect(administerManage)
#管理员修改食材

def adminChangeIngredients(request,id):
    error_msg = ''
    form = IngredientsForm()
    if request.method == 'POST':
        try:
            form.setPost(request.POST)
        except Exception:
            error_msg = '数据格式不正确'
        else:
            Query_ingredients = IngredientsInfo.objects.filter(ingredientsName=form.ingredientsName)
            if len(Query_ingredients) >= 2:
                error_msg = '用户名已存在'
            else:
                IngredientsInfo.objects.filter(id=id).update(ingredientsName=form.ingredientsName, water=form.water,
                                                      energy=form.energy, protein=form.protein, fat=form.fat,
                                                             saccharides=form.saccharides, price=form.price)
                return redirect(administerManage)
    return render(request, 'administerManage.html', {'error_msg': error_msg})
# 管理员查询食材

def adminSearchIngredients(request):
    error_msg = ''
    if request.method == 'POST':
        researchingredients = request.POST['ingredientsName']
        print(researchingredients)
        if researchingredients == "":
            error_msg = '请输入食材名搜索'
            user_list = UserInfo.objects.all()
            ingredients_list =IngredientsInfo.objects.all()
            return render(request, 'administerManage.html',
                          {'user_list': user_list, 'ingredients_list': ingredients_list, 'error_msg': error_msg})
        else:
            ingredientsName = IngredientsInfo.objects.filter(ingredientsName__contains=researchingredients)
            print(ingredientsName)
            if len(ingredientsName) >= 1:
                user_list = UserInfo.objects.all()
                ingredients_list = ingredientsName
                dish_list=DishInfo.objects.all()
                return render(request, 'administerManage.html',
                              {'user_list': user_list, 'ingredients_list': ingredients_list,'dish_list':dish_list})
            else:
                error_msg = '不存在该食材'
                user_list = UserInfo.objects.all()
                return render(request, 'administerManage.html',
                              {'user_list': user_list, 'error_msg': error_msg})
    return render(request, 'administerManage.html', {'error_msg': error_msg})



def display(request):
    context = {}
    return render(request, 'display.html', context)


def userManage(request):
    try:
        id = request.session['user_id']
    except Exception:
        return render(request, 'userLogin.html')
    user = UserInfo.objects.get(id=id)
    context = {'user': user}
    return render(request, 'userManage.html', context)


def I_changeUser(request,id):
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
                user_list = UserInfo.objects.all()
        return redirect(userManage)
    return render(request, 'userManage.html', {'error_msg': error_msg})

