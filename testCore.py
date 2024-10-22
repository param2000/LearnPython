from Core import *
from Util import addItem

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
    assert items["apple"]==1
    addItem(items, "apple")
    assert 2 == items["apple"]
