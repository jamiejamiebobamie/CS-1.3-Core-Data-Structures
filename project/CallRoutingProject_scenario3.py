
#SCENARIO #3

"""

Similar solution to solution #1, but the functions find the lowest costs for all
phone numbers in the file.

"""

import sys
import os
import glob


routes = glob.glob('/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/routeLists/*.txt')
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-3.txt'

def createRouteCostDictionary(files):
    """Time complexity: O(n**2). Space complexity O(2n).
    Read each file in the list of files and split the lines of each file
    into an array. Read the array and return a dictionary of routes to costs."""
    dictionary = {}
    for file in files:
        f = open(str(file))
        lines = f.read().split()
        f.close()
        for line in lines:
            route, cost=line.split(",")
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
            else:
                continue
        if minimum != float('inf'):
            file += str(phoneNumber)+','+ str(minimum)+'\n'
        else:
            file += str(phoneNumber)+','+ str(0)+'\n'

    return file

print(findLowestCost(createRouteCostDictionary(routes), readPhoneNumbers(numbers)))
