"""
SCENARIO #3

This program builds a Trie from the routes in the routeList files at
./project/data/routeLists.

For each digit of a route, a node is added to the the tree.

The ancestors of a node are the digits that come before it in the route.

For example, the route "+1234" appears in the tree as:

                root
                 +
                1
            2
        3
    4

If the route "+1233" was then added, the tree would add a single new node of "3" after the "3".
The new tree would look like this:

                root
                 +
                1
            2
        3
      4   3


While it takes a very long time to build the Trie, the lookup time is the length of the phone number.

This solution assumes you have already built the Trie and it exists somewhere in memory.

"""

import sys
import os
import glob

routes = glob.glob('/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/routeLists/*.txt')
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-10000.txt'

class Trie:
    """A Trie to hold the digits of a route and its associated cost."""

    def __init__(self, routeFiles):
        self.root = self.TrieNode()
        for routeFile in routeFiles:
            self.buildTrieOfRoutes(routeFile)

    class TrieNode:
        def __init__(self, value=None):
            self.value = value
            self.dictionary = {}
            self.cost = None

    def buildTrieOfRoutes(self, file):
        """Takes in a file with lines of 'route,costs' and builds a Trie of the routes' digits."""

        for line in open(file):
            current = self.root
            route, cost=line.split(",")
            cost = float(cost.strip("\n"))
            for digit in route:
                if digit not in current.dictionary:
                    current.dictionary[digit] = self.TrieNode(digit)
                current = current.dictionary[digit]
            if current.cost:
                if current.cost > cost:
                    current.cost = cost
            else:
                current.cost = cost

    def findLowestCostsAndPrintThemToFile(self, file):
        """Finds the lowest costs for each phone number in the input file."""

        for phoneNumber in open(file):
            current = self.root
            minimum = float('inf')
            for digit in phoneNumber:
                if digit in current.dictionary:
                    if current.cost:
                        minimum = min(minimum, current.cost)
                    current = current.dictionary[digit]
                else:
                    break # break out of the 'for digit in phoneNumber' loop
            phoneNumber = phoneNumber.strip("\n")
            if minimum != float('inf'):
                with open("output_logs/route-costs-3.txt", "a+") as f:
                        f.write(phoneNumber + ", " + str(minimum) + '\n')
            else:
                with open("output_logs/route-costs-3.txt", "a+") as f:
                        f.write(phoneNumber + ", 0 \n")


if __name__ == "__main__":
    new = Trie(routes)
    print("Done building Trie.")
    new.findLowestCostsAndPrintThemToFile(numbers)
