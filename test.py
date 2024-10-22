from Core import *
from HttpPlay import *
from Util import addItem
import pytest

dis = 1==0

def test_add():
    assert getTotal(5, 5)==10

def test_frizzbeebuzz():
    result = frizzBeeBuzz(15)
    assert result == "frizzbeebuzz"

def test_frizzbeebuzz():
    result = frizzBeeBuzz(3)
    assert result == "frizzbee"

def test_frizzbeebuzz():
    result = frizzBeeBuzz(5)
    assert result == "buzz"

def test_frizzbeebuzz():
    result = frizzBeeBuzz(7)
    assert result == "None"

def test_frizzbeebuzz():
    result = frizzBeeBuzz(-7)
    assert result == "None"




if dis:

    z = getList(10)
    print(z)

    temp = 10
    a = getDictionary(temp)
    print(a)

    for i in range(temp,temp+10):
        print(a.get(i))

url = "https://www.themealdb.com/api/json/v1/1/categories.php"
urlVeggie = "https://www.themealdb.com/api/json/v1/1/filter.php?c=vegetarian"
urlMeal ="https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"

httpPlay = HttpPlay()
items = {}
addItem(items, "apple")
addItem(items, "apple")
print(items)
#print(httpPlay.getResponse(urlVeggie))
#print(httpPlay.getResponse2(urlMeal))
#print(httpPlay.getResponse(urlVeggie))
#print(httpPlay.getAllVeggieMeals(urlVeggie))

meals = httpPlay.getAllVeggieMeals(urlVeggie)
#print(meals)
allVeggiesIngredientCount = httpPlay.getIngredientsForAMeal(meals)
print(allVeggiesIngredientCount)
sortedItems= dict(sorted(allVeggiesIngredientCount.items(), key = lambda x:x[1], reverse = True))
print(sortedItems)

