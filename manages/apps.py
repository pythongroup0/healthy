from django.apps import AppConfig


class ManagesConfig(AppConfig):
    name = 'manages'

class addDishForm():
    dishName = ''
    dishEnergy = ''
    dishPrice = ''
    dishClassify=''
    dishIngredients=''

    def setPost(self,post):
        self.dishName = post['dishName']
        self.dishEnergy = float(post['dishEnergy'])
        self.dishPrice = float(post['dishPrice'])
        self.dishClassify = post['dishClassify']
        self.dishIngredients=post['dishIngredients']


class IngredientsForm():
    ingredientsName = ''
    energy = 0
    protein = 0.0
    fat = 0.0
    saccharides= 0.0
    price=0.0

    def setPost(self,post):
        self.ingredientsName = post['ingredientsName']
        self.energy  = int(post['energy'])
        self.protein = float(post['protein'])
        self.fat =float( post['fat'])
        self.saccharides =float( post['saccharides'])
        self.price=float(post['price'])