
"""
SCENARIO #1

As there is no order to the routes in the route file, the entirety of the file
has to be read.

Open the file. Iterate through it. Searching each digit of each route.
If the program reaches the end of a route, we check to see if that route is cheaper than the current
lowest price and change the lowest to that route's cost if it is.

Finally returning the lowestRouteCost when all routes in the route file have been read.

Call the function in the terminal with the desired phone number to lookup.
This function assumes their is a fixed route file list that is hardcoded into the function.

"""

import sys

routes = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/route-costs-4.txt'
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-3.txt'

def iterateThroughRoutesFile(routesFile, phoneNumber):
    """Time complexity: O(n**2), n being the number of routes and the length of their digits.
        Space complexity: O(1), the lowestRouteCost variable."""
    lowestRouteCost = float('inf')

    for line in open(routesFile):
        i = 0 # index
        route, cost=line.split(",")# O(n)
        while route[i] == phoneNumber[i] and i < len(route) - 1:
            i += 1
        else:
            if i == len(route) - 1:
                cost = float(cost.strip("\n")) #O(n)
                if lowestRouteCost > cost:
                    lowestRouteCost = cost
    return lowestRouteCost if lowestRouteCost != float('inf') else "Your route does not exist."


if __name__ == "__main__":
    phoneNumber = str(sys.argv[1])
    print(iterateThroughRoutesFile(routes, phoneNumber))
