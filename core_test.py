from Core import Core
from Util import *


def test_add():
    assert Core.getTotal(5, 5)==10

def test_frizzbeebuzz():
    result = Core.frizzBeeBuzz(15)
    assert result == "frizzbeebuzz"

def test_frizzbeebuzz():
    result = Core.frizzBeeBuzz(3)
    assert result == "frizzbee"

def test_frizzbeebuzz():
    result = Core.frizzBeeBuzz(5)
    assert result == "buzz"

def test_frizzbeebuzz():
    result = Core.frizzBeeBuzz(7)
    assert result == None

def test_frizzbeebuzz():
    result = Core.frizzBeeBuzz(-7)
    assert result == None

def test_addingCount():
    items ={}
    addItem(items, "apple")
    assert items["apple"]==1
    addItem(items, "apple")
    assert 2 == items["apple"]

def test_dictionary():
    a = Core.getDictionary(10)
    print(a)
    assert len(a)==10

def test_list():
    a = Core.getList(10)
    print(a)
    assert len(a)==10

