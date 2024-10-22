from typing import List, Any
import inflect


def getTotal(a, b):
    return a + b


def getList(a):
    elements: list[int | Any] = []
    for i in range(10):
        a = a + 1
        #print(a)
        elements.append(a)
    return elements


def getDictionary(a):
    elements = {}
    p = inflect.engine()
    for i in range(10):
        elements[a] = p.number_to_words(a)
        #print(a)
        #print(p.number_to_words(a))
        a=a+1
    return elements


def frizzBeeBuzz(n):
    if n<=0: return None
    if n%3==0 and n%5==0: return "frizzbeebuzz"
    if n%3==0: return "frizzbee"
    if n%5==0: return "buzz"
    return None
