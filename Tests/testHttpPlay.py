from Core import getList, getDictionary
from HttpPlay import HttpPlay
from testHttpPlay import z, temp, a, allVeggiesIngredientCount, sortedItems


dis = 1==0

if dis:

    print(z)

    print(a)

    for i in range(temp, temp + 10):
        print(a.get(i))

#print(httpPlay.getResponse(urlVeggie))
#print(httpPlay.getResponse2(urlMeal))
#print(httpPlay.getResponse(urlVeggie))
#print(httpPlay.getAllVeggieMeals(urlVeggie))

#print(meals)
print(allVeggiesIngredientCount)
print(sortedItems)



z = getList(10)
temp = 10
a = getDictionary(temp)
url = "https://www.themealdb.com/api/json/v1/1/categories.php"
urlVeggie = "https://www.themealdb.com/api/json/v1/1/filter.php?c=vegetarian"
urlMeal ="https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"
httpPlay = HttpPlay()
meals = httpPlay.getAllVeggieMeals(urlVeggie)
allVeggiesIngredientCount = httpPlay.getIngredientsForAMeal(meals)
sortedItems= dict(sorted(allVeggiesIngredientCount.items(), key = lambda x:x[1], reverse = True))
