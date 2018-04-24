from django.apps import AppConfig


class ManagesConfig(AppConfig):
    name = 'manages'

class addDishForm():
    dishName = ''
    dishEnergy = ''
    dishPrice = ''

    def setPost(self,post):
        self.dishName = post['dishName']
        self.dishEnergy = float(post['dishEnergy'])
        self.dishPrice = float(post['dishPrice'])

class IngredientsForm():
    ingredientsName = ''
    water = 0.0
    energy = 0
    protein = 0.0
    fat = 0.0
    saccharides= 0.0
    price=0.0

    def setPost(self,post):
        self.ingredientsName = post['ingredientsName']
        self.water = float(post['water'])
        self.energy  = int(post['energy'])
        self.protein = float(post['protein'])
        self.fat =float( post['fat'])
        self.saccharides =float( post['saccharides'])
        self.price=float(post['price'])