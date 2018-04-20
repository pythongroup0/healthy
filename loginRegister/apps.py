from django.apps import AppConfig


class LoginregisterConfig(AppConfig):
    name = 'loginRegister'

class UserLoginForm():
    def __init__(self,username='',password=''):
        self.username = username
        self.password = password
    def setPost(self,post):
        self.username = post['username']
        self.password = post['password']

class AdminLoginForm():
    def __init__(self,adminname='',password=''):
        self.adminname = adminname
        self.password = password
    def setPost(self,post):
        self.adminname = post['adminname']
        self.password = post['password']

class UserRegisterForm():
    username = ''
    password = ''
    email=''
    sex = True
    height = 0
    weight = 0
    age = 0
    allergic_food = ''
    taste = ''

    def setPost(self,post):
        self.username = post['username']
        self.password = post['password']
        self.email = post['email']
        self.sex = bool(post['sex'])
        self.height = float(post['height'])
        self.weight = float(post['weight'])
        self.age = float(post['age'])
        self.allergic_food = post['allergic_food']
        self.taste = post['taste']
