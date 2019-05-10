
#SCENARIO #2

import timeit


"""

Similar solution to solution #1, but the functions find the lowest costs for all
phone numbers in the file.

"""

routes = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/route-costs-1000000.txt'
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-1000.txt'

def createRouteCostDictionary(filePath):
    """Time complexity: O(2n). Space complexity O(2n).
    Read the file and split the lines into an array.
    Read the array and return a dictionary of routes to costs."""
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

def readPhoneNumbers(filePath):
    """Time complexity: O(n). Space complexity O(n).
    Read the file and split the lines into an array. Return the array."""
    f = open(str(filePath))
    numbersArray = f.read().split()
    f.close()

    return numbersArray

def findLowestCost(routes, phoneNumbers):
    """Time complexity: O(n**3). Space complexity O(2n).

    Iterate through each phone number in the array of phone numbers,
    for each number grow a 'test' string by adding each digit.
    Test if that 'test' string is a key in the dictionary.
    If it is, check to see if it is the lowest cost for that number.
    If the 'test' string is not in the dictionary then, move onto
    the next phone number after adding that phone number and it's lowest cost to
    the output file.

    A string concatenation inside a nested for loop makes this function have
    an 'n-cubed' time complexity."""

    file = ""
    for phoneNumber in phoneNumbers:
        test = ""
        minimum = float('inf')
        for digit in phoneNumber:
            test += digit
            if test in routes:
                minimum = min(minimum,float(routes[test]))
        if minimum != float('inf'):
            file += str(phoneNumber)+','+ str(minimum)+'\n'
        else:
            file += str(phoneNumber)+','+ str(0)+'\n'

    return file

print(findLowestCost(createRouteCostDictionary(routes), readPhoneNumbers(numbers)))



# t = Timer()       # outside the try/except
# try:
#     t.timeit(...)    # or t.repeat(...)
# except:
#     t.print_exc()
