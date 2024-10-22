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
        # concatenation is bad for request forgery, but for fun it's Okay
        url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + meal["id"]
        ingredients = requests.get(url).json()
        for ingredient in ingredients["meals"]:
            addIngredients(ingredient, items)
    return items


def addIngredients(ingredient, items):
    for key in ingredient:
        if key.startswith("strIngredient") and ingredient[key] != "":
            addItem(items, ingredient[key])

