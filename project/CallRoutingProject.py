

routes = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/route-costs-4.txt'
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-3.txt'

def createRouteCostDictionary(filePath):

    f = open(str(filePath))
    lines = f.read().split()
    f.close()
    dictionary = {}
    for line in lines:
        route, cost=line.split(",")
        dictionary[route] = cost

    return dictionary

def readPhoneNumbers(filePath):
        f = open(str(filePath))
        numbersArray = f.read().split()
        f.close()

        return numbersArray
