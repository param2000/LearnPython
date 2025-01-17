import requests
from Util import *

class HttpPlay:

    @staticmethod
    def getResponse(url):
        response = requests.get(url)
        return response.json()

    @staticmethod
    def getResponse2(url):
        response = requests.get(url)
        meals = response.json()["meals"]
        #for meal in meals:
            #print(meal["idMeal"])
            #print(meal["strMeal"])
        return

    @staticmethod
    def getAllVeggieMeals(url):
        response = requests.get(url)
        meals = response.json()["meals"]
        veggies = []
        for meal in meals:
            veggies.append({"id" : meal["idMeal"], "name": meal["strMeal"]})
        return {"meals" :veggies}

    def getIngredientsForAMeal(self, meals):
        items = {}
        for meal in meals["meals"]:
            # concatenation is bad for request forgery, but for fun it's Okay
            url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + meal["id"]
            ingredients = requests.get(url).json()
            for ingredient in ingredients["meals"]:
                self.addIngredients(ingredient, items)
        return items

    @staticmethod
    def addIngredients(ingredient, items):
        for key in ingredient:
            if key.startswith("strIngredient") and ingredient[key] != "":
                addItem(items, ingredient[key])

