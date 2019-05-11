"""
SCENARIO #3

Similar solution to solution #1 and #2, but the functions find the lowest costs for all
phone numbers in the routeLists foldr by using the python package glob.

"""

import sys
import os
import glob

routes = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/route-costs-1000000.txt'
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-10000.txt'



'''An autocomplete function. Call the function in the terminal and
    type a prefix to see all possibile words that can be made with that prefix.

Input:  python3 autocompleteWithClasses.py lla
Output: ['llama', 'llanberisslate', 'llandeilo', 'llandovery', 'llano', 'llautu']

TO-DO: Rewrite code in Javascript and then make a website
       that hosts the already built Trie in a database and pulls from it
       dynamically, displaying the possibile words in a drop-down menu as the user types.

       Find out how much 'overhead', it costs to have these extra properties in the TrieNode.
       (self.count and self.depth).'''

import sys

class Trie:
    """A Trie specificially made to hold a dictionary of words."""

    def __init__(self, fileOfRoutes):
        self.root = self.buildTrieOfRoutes(fileOfRoutes)

    class TrieNode:
        def __init__(self, value=None, i=None):
            self.value = value
            self.dict = {}
            self.cost = None

#How many routes contain this prefix:
            self.count = 0

#How many digits into the route, 0 = first letter:
            self.depth = i

    def buildTrieOfRoutes(self, file):
        """Takes in a file with lines of 'route,costs' and builds a Trie of the routes' digits."""
        root = current = self.TrieNode()
        for line in open(file):
            route, cost=line.split(",")
            for i, digit in enumerate(route):
                if digit not in current.dict:
                    current.dict[digit] = self.TrieNode(digit,i)
                current.count += 1
                current = current.dict[digit]
            if current.cost: #rewrite... there is a definitely more succinct way of writing this logic.
                if current.cost > cost:
                    current.cost = cost
            else:
                current.cost = cost
            current = root
        return root

    def findLowestCosts(self, file):
        """Finds the lowest costs for each phone number in the input file where
        each line is a phone number. Returns an array of

        Uses a recursive helper function to traverse the Trie."""

        def __findWordsHelper(node, w):
            """Takes in the current node and the string built so far.
            Iterates through the Trie,
            appending all possible words to the 'words' array."""

            for key in node.dict:
                word = w #passing off the built word to the interior scope.
                word += node.dict[key].value
                if node.dict[key].end == True:
                    words.append(word)
                __findWordsHelper(node.dict[key], word)

        costs = []

        for phoneNumber in open(file):
            # print(phoneNumber)
            current = previous = self.root
            for digit in phoneNumber:
                if digit in current.dict:
                    previous = current
                    current = current.dict[digit]
                else:
                    costs.append((phoneNumber,current.cost))

        # __findWordsHelper(current, prefix)
        return costs

new = Trie(routes)
print(new.findLowestCosts(numbers))


# if __name__ == "__main__":
#     prefix = str(sys.argv[1]).lower() #note: uppercase letters would otherwise affect output
#     new = Trie()
#     print(new.findWords(prefix))
