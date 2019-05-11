"""
SCENARIO #3

This program builds a Trie from the routes in the routeList files at
./project/data/routeLists.

For each digit of a route, a node is added to the the tree.

The ancestors of a give node are the digits that come before it in the route.

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


While it takes a very long time to build the Trie, the lookup time is O(1).

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
            self.previous = None

    def buildTrieOfRoutes(self, file):
        """Takes in a file with lines of 'route,costs' and builds a Trie of the routes' digits."""

        for line in open(file):
            current = previous = self.root
            route, cost=line.split(",")
            cost = float(cost.strip("\n"))
            for digit in route:
                if digit not in current.dictionary:
                    current.dictionary[digit] = self.TrieNode(digit)
                previous = current
                current = current.dictionary[digit]
                current.previous = previous
            if current.cost:
                if current.cost > cost:
                    current.cost = cost
            else:
                current.cost = cost

    def findLowestCosts(self, file):
        """Finds the lowest costs for each phone number in the input file.
        Uses a recursive helper function to traverse the Trie."""

        costs = []

        for phoneNumber in open(file):
            current = self.root
            for digit in phoneNumber:
                if digit in current.dictionary:
                    current = current.dictionary[digit]
                else:
                    # we have to go back toward the root until we find an
                    # ancestor of the current node that has a cost
                    # associated with it.
                    while current and not current.cost:
                        current = current.previous
                    else:
                        phoneNumber = phoneNumber.strip("\n")
                        if current and current.cost:
                            costs.append((phoneNumber,current.cost))
                        else:
                            costs.append((phoneNumber, 0))
                    break

        return costs

new = Trie(routes)
print("Done building Trie.")
print(new.findLowestCosts(numbers))


if __name__ == "__main__":
    new = Trie(routes)
    print("Done building Trie.")
    print(new.findLowestCosts(numbers))
