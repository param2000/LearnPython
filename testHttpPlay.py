from Core import getList, getDictionary
from HttpPlay import HttpPlay

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
