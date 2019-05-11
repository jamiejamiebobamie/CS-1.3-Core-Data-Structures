"""
SCENARIO #3



"""

import sys
import os
import glob

routes = glob.glob('/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/routeLists/*.txt')
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-10000.txt'

class Trie:
    """A Trie specificially made to hold the digits of a route and its associated cost."""

    def __init__(self, routeFiles):
        self.root = self.TrieNode()
        for routeFile in routeFiles:
            self.buildTrieOfRoutes(routeFile)

    class TrieNode:
        def __init__(self, value=None):
            self.value = value
            self.dict = {}
            self.cost = None
            self.last = None

    def buildTrieOfRoutes(self, file):
        """Takes in a file with lines of 'route,costs' and builds a Trie of the routes' digits."""
        current = self.root
        for line in open(file):
            route, cost=line.split(",")
            for digit in route:
                if digit not in current.dict:
                    current.dict[digit] = self.TrieNode(digit)
                current = current.dict[digit]
            if current.cost: #rewrite... there is a definitely more succinct way of writing this logic.
                if current.cost > cost:
                    current.cost = cost
            else:
                current.cost = cost
            current = self.root

    def findLowestCosts(self, file):
        """Finds the lowest costs for each phone number in the input file.
        Uses a recursive helper function to traverse the Trie."""

        # def __findCostsHelper(trieNode, testKey):
        #     """Takes in the current trieNode and the testKey built so far.
        #     Iterates through the Trie,
        #     appending all possible words to the 'words' array."""
        #
        #     for key in node.dict:
        #         test = testKey #passing off the built word to the interior scope.
        #         word += node.dict[key].value
        #         if node.dict[key].end == True:
        #             words.append(word)
        #         __findWordsHelper(node.dict[key], word)
        #
        costs = []

        for phoneNumber in open(file):
            current = previous = self.root
            for i, digit in enumerate(phoneNumber):
                if digit in current.dict:
                    previous = current
                    current = current.dict[digit]
                else:
                    if digit in current.dict:
                        if current.dict[digit].cost:# need to make a previous node pointer...
                            costs.append((phoneNumber,current.dict[digit].cost))

        # __findWordsHelper(current, prefix)
        return costs

new = Trie(routes)
# print(new.root.dict)
print(new.findLowestCosts(numbers))


# if __name__ == "__main__":
#     prefix = str(sys.argv[1]).lower() #note: uppercase letters would otherwise affect output
#     new = Trie()
#     print(new.findWords(prefix))
