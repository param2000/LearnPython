from os import system
import Core
from Core import getTotal, getList, getDictionary, frizzBeeBuzz
from HttpPlay import *

x = getTotal(5,5)
print(x)
dis = 1==0
if dis:
    z = getList(10)
    print(z)

    temp = 10
    a = getDictionary(temp)
    print(a)

    for i in range(temp,temp+10):
        print(a.get(i))

    print(frizzBeeBuzz(15))
    print(frizzBeeBuzz(3))
    print(frizzBeeBuzz(5))
    print(frizzBeeBuzz(7))

    items = {}
    addItem(items, "apple")
    addItem(items, "apple")
    print(items)

url = "https://www.themealdb.com/api/json/v1/1/categories.php"
urlVeggie = "https://www.themealdb.com/api/json/v1/1/filter.php?c=vegetarian"
urlMeal ="https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"

#print(getResponse(urlVeggie))
#print(getResponse2(urlMeal))
#print(getResponse(urlVeggie))

#print(getAllVeggieMeals(urlVeggie))
meals =getAllVeggieMeals(urlVeggie)
#print(meals)
allVeggiesIngredientCount = getIngredientsForAMeal(meals)
print(allVeggiesIngredientCount)
sortedItems= dict(sorted(allVeggiesIngredientCount.items(), key = lambda x:x[1], reverse = True))
print(sortedItems)

