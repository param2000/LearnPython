import inflect

class Core:
    @staticmethod
    def getTotal(a, b):
        return a + b

    @staticmethod
    def getList(a):
        elements=[]
        for i in range(10):
            a += 1
            elements.append(a)
        return elements

    @staticmethod
    def getDictionary(a):
        elements = {}
        p = inflect.engine()
        for i in range(10):
            elements[a] = p.number_to_words(a)
            a+=1
        return elements

    @staticmethod
    def frizzBeeBuzz(n):
        if n<=0: return None
        if n%3==0 and n%5==0: return "frizzbeebuzz"
        if n%3==0: return "frizzbee"
        if n%5==0: return "buzz"
        return None
