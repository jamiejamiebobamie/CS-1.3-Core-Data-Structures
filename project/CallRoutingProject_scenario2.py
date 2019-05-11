
#SCENARIO #2

"""
There is no order to the routes in the route file, so the entirety of the file
has to be read. Because each route has a cost associated with it, it makes sense
to create a dictionary of routes to costs, key-value pairs.

Iterate over the route-costs in the routeFile and create a a dictionary of routes to costs, key-value pairs.
Iterate over the phoneNumbers file and split each line into an array.

Feed that array of phoneNumbers into a function that concatenates a test string composed of digits of a phoneNumber
and test if that test-strign is a key in the dictionary. If it is, return the cost associated with that number.

Return an array of tuples that consist of phoneNumbers and their associated costs.


"""

routes = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/route-costs-10000000.txt'
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-1000.txt'

def createRouteCostDictionary(routesFile):
    """Time complexity: O(2n*m), Space complexity O(2n+m).
    n, the number of lines in the file.
    m, the number of characters in the line.

    Read the file and split the lines into an array of two elements: [route,cost].
    Read the array and return a dictionary of routes to costs."""

    dictionary = {}
    for line in open(routesFile):
        route, cost=line.split(",")
        if route in dictionary:
            if dictionary[route] > cost:
                dictionary[route] = cost
        else:
            dictionary[route] = cost

    return dictionary

def readPhoneNumbers(filePath):
    """Time complexity: O(n). Space complexity O(n).
    Read the file and split the lines into an array. Return the array."""

    f = open(str(filePath))
    numbersArray = f.read().split()
    f.close()
    return numbersArray

def findLowestCost(routes, phoneNumbers):
    """Time complexity: O(n**2). Space complexity O(2n).

    Iterate through the digits of the phone number, growing a 'test' string
    by adding each digit. Test if that 'test' string is a key in the dictionary.

    If it is, check to see if it is the lowest cost for that number.

    If the 'test' string is not in the dictionary then return the result.

    As there is only one string to iterate through while concatenating a 'test'
    string-key, this function has an O(n**2) time complexity."""

    test = ""
    minimum = float('inf')
    results = []
    print(len(phoneNumbers))
    for phoneNumber in phoneNumbers: # O(n)
        for digit in phoneNumber:
            test += digit # O(n) <-- nested
            if test in routes:
                minimum = min(minimum,float(routes[test]))
            else:
                if minimum != float('inf'):
                    results.append((phoneNumber, str(minimum)))
                else:
                    results.append((phoneNumber, "Your route does not exist."))
    return results

print(findLowestCost(createRouteCostDictionary(routes), readPhoneNumbers(numbers)))
