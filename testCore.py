from Core import *
from Util import addItem

from testHttpPlay import z, temp, a, allVeggiesIngredientCount, sortedItems

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

def test_addingCount():
    items ={}
    addItem(items, "apple")
    #print(items)
    assert items["apple"]==1

    addItem(items, "apple")
    assert 2 == items["apple"]


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

