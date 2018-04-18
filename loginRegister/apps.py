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