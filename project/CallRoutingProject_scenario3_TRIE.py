
#SCENARIO #3

"""

Similar solution to solution #1 and #2, but the functions find the lowest costs for all
phone numbers in the routeLists foldr by using the python package glob.

"""

import sys
import os
import glob


routes = glob.glob('/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/routeLists/*.txt')
numbers = '/Users/jamesmccrory/documents/dev/CS-1.3-Core-Data-Structures/project/data/phone-numbers-3.txt'

def buildTheTrieOfRoutes(files):
    """Time complexity: O(n**2). Space complexity O(2n).
    Read each file in the list of files and split the lines of each file
    into an array. Read the array and return a dictionary of routes to costs."""
    for file in files:
        f = open(str(file))
        lines = f.read().split()
        f.close()
        for line in lines:
            route, cost=line.split(",")
            for digit in route:
                # if it is the last digit, add the TrieNode for the digit and the cost for the route.
                # if it is not the last digit in the route add just the TrieNode for the digit.
                pass

def readPhoneNumbersAndFindLowestCosts(filePath):
    """Time complexity: O(n). Space complexity O(n).
    Read the file and split the lines into an array. Return the array."""
    for phoneNumber in open('/usr/share/dict/words'):
        for digit in phoneNumber:
            # pass each digit into the Trie and find the lowest cost
            pass



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

    def __init__(self):
        self.root = self.buildTrie(self.dict())

    class TrieNode:
        def __init__(self, value=None, i=None):
            self.value = value
            self.dict = {}
            self.end = False

#How many words contain this prefix:
            self.count = 0

#How many letters into the word, 0 = first letter:
            self.depth = i

    def buildTrie(self, array):
        """Takes in an array of strings and builds a Trie of the strings' characters."""

        root = self.TrieNode()
        current = root
        for word in array:
            for i, char in enumerate(word):
                c = char.lower()
                if c not in current.dict:
                    current.dict[c] = self.TrieNode(c,i)
                current.count += 1
                current = current.dict[c]
            current.end = True
            current = root
        return root

    def dict(self):
        """Opens the dictionary-words file at the path. Assigns the file to 'f'.
        Reads 'f' and splits each word into a 'words' array element.
        Closes 'f'. Returns the array of dictionary words."""

        f = open("/usr/share/dict/words", "r")
        words = f.read().split()
        f.close()
        return words

    def findWords(self, prefix):
        """Finds words that can be made with the prefix.
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

        words = []
        current = self.root

#Move up to the correct point in the dictionary:
        for char in prefix:
            if char in current.dict:
                current = current.dict[char]
            else:
                return []

#Recursive function. Iterate through all nodes:
        __findWordsHelper(current, prefix)
        return words

if __name__ == "__main__":
    prefix = str(sys.argv[1]).lower() #note: uppercase letters would otherwise affect output
    new = Trie()
    print(new.findWords(prefix))
