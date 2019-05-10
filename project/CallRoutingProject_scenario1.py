
#SCENARIO #1

"""
As there is no order to the routes in the route file, the entirety of the file
has to be read. Because each route has a cost associated with it, it makes sense
to create a dictionary of routes to costs, key-value pairs.

But having only one number to check seems to elimate a large portion
of the possible routes. So it seems wasteful and more work than is necessary
to create an entire dictionary...

If there was some way to iterate through the file and check
line by line for subsets of the phone number in the routes,
the time complexity would still be O(n**2), but the check would require
one function and be more succinct.
"""

routes = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/route-costs-4.txt'
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-3.txt'

def createRouteCostDictionary(filePath):
    """Time complexity: O(2n+m), Space complexity O(2n+m),
    n the length of all the characters in the file,
    and m the number of lines in the file (which become array elements).

    Read the file and split the lines into an array.
    Read the array and return a dictionary of routes to costs.

    TO-DO: Create the dictionary with one pass over the file."""

    f = open(str(filePath))
    lines = f.read().split()
    f.close()
    dictionary = {}
    for line in lines:
        route, cost=line.split(",")
        if dictionary.get(route, None): # check to see if the entry exists in the dictionary
            if dictionary[route] > cost:
                dictionary[route] = cost
        else:
            dictionary[route] = cost

    return dictionary

def readPhoneNumber(filePath):
    """Time complexity: O(n). Space complexity O(n),
    the length of the phone number.

    Read the first line of the file and return the phone number."""
    f = open(str(filePath))
    phoneNumber = f.readline().strip('\n')
    f.close()

    return phoneNumber

def findLowestCost(routes, phoneNumber):
    """Time complexity: O(n**2). Space complexity O(2n).

    Iterate through the digits of the phone number, growing a 'test' string
    by adding each digit. Test if that 'test' string is a key in the dictionary.

    If it is, check to see if it is the lowest cost for that number.

    If the 'test' string is not in the dictionary then return the result.

    As there is only one string to iterate through while concatenating a 'test'
    string-key this function has an O(n**2) time complexity."""

    test = ""
    minimum = float('inf')
    result = ""

    for digit in phoneNumber:
        test = test.join(digit)
        if test in routes:
            minimum = min(minimum,float(routes[test]))
        else:
            if minimum != float('inf'):
                result = str(phoneNumber)+','+ str(minimum)
            else:
                result = str(phoneNumber)+','+ str(0)
    return result

print(findLowestCost(createRouteCostDictionary(routes), readPhoneNumber(numbers)))
