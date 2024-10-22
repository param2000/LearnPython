from Core import getList, getDictionary
from HttpPlay import HttpPlay

url = "https://www.themealdb.com/api/json/v1/1/categories.php"
urlVeggie = "https://www.themealdb.com/api/json/v1/1/filter.php?c=vegetarian"
urlMeal ="https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"
httpPlay = HttpPlay()

def test_json_data_structure():
    result = httpPlay.getAllVeggieMeals(urlVeggie)
    assert result is not None
    assert type(result) is dict


def test_json_data_from_response():
    result = httpPlay.getResponse(urlVeggie)
    assert result is not None
    assert type(result) is dict


def test_json_data_from_response_2():
    result = httpPlay.getResponse2(urlMeal)
    #print(result)
    assert result is None


def test_json_data_fromAllVeggies():
    result = httpPlay.getAllVeggieMeals(urlVeggie)
    assert result is not None
    assert type(result) is dict

def test_AllIngredientsCountColleted():
    meals = httpPlay.getAllVeggieMeals(urlVeggie)
    #print(meals)
    allVeggiesIngredientCount = httpPlay.getIngredientsForAMeal(meals)
    sortedItems= dict(sorted(allVeggiesIngredientCount.items(), key = lambda x:x[1], reverse = True))
    #print(sortedItems)

    assert sortedItems is not None
    assert type(sortedItems) is dict
    assert sortedItems.keys() is not None
    assert sortedItems.values() is not None

    assert sortedItems["Olive Oil"] == 22

