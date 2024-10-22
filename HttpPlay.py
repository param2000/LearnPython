import requests
import json

def getResponse(url):
    response = requests.get(url)
    return response.json()

def getResponse2(url):
    response = requests.get(url)
    meals = response.json()["meals"]
    for meal in meals:
        print(meal["idMeal"])
        print(meal["strMeal"])
    return
def getAllVeggieMeals(url):
    response = requests.get(url)
    meals = response.json()["meals"]
    veggies = []
    for meal in meals:
        #print(meal["idMeal"])
        #print(meal["strMeal"])
        #veggies.append({meal["idMeal"]:meal["strMeal"]})
        veggies.append({"id" : meal["idMeal"], "name": meal["strMeal"]})
    return {"meals" :veggies}


def addItem(items, key):
    if key in items:
        items[key] += 1
        return
    items[key] = 1
    return


def getIngredientsForAMeal(meals):
    items = {}
    for meal in meals["meals"]:
        #print(meal)
        url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + meal["id"]
        #print(url)
        ingredients = requests.get(url).json()
        #print(ingredients)
        for ingredient in ingredients["meals"]:
            #print(ingredient)
            for key in ingredient:
                #print(key)
                if key.startswith("strIngredient") and ingredient[key] != "":
                    #print(ingredient[key])
                    addItem(items, ingredient[key])

    return items

