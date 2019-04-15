# Write unit tests to ensure the Set class is robust
# Include test cases for each class instance method
# Annotate all instance methods with complexity analysis of running time and space (memory)
# Compare the behaviors of your Set class to those of the Python set type and Swift Set type
class Set(object):

    def __init___(elements=None):
        self.container = {}
        self.size = 0
        for element in elements:
            self.add(element)

    def contains(element):
        if element in self.container:
            return True

    def add(element):
        if not self.contains(element):
            self.container[element] = 1
            self.size += 1

    def remove(element):
        if self.contains(element):
            self.container.pop('element', None)
            self.size -= 1
        else:
            raise KeyError("Element not in set.")

    def union(other_set):
        """Iterate over two sets and create a new set from the elemets contained in both.
        This method is meant to decrease overall time complexity by iterating
        over an element once. The space complexity is high as the other_set is duplicated
        in order to pop elements from it.

        TO-DO: Perhaps write an if-statement that begins the function that causes the program
        to follow a different set of instructions if the size of the other_set exceeds a given
        amount."""

        new_set = Set()

        other_set_copy = other_set

        for element in self.container:

            if other_set_copy.contains(element):
                other_set_copy.remove(element)

            new_set.add(element)

        for element in other_set_copy.container:
            new_set.add(element)


    def intersection(other_set):
    """Iterate through the smaller set and look for items contained
            in both sets and add them to a new set."""

        new_set = Set()

        if self.size > other_set.size:
            for element in other_set.container:
                if self.contains(element):
                    new_set.add(element)
        else:
            for element in self.container:
                if other_set.contains(element):
                    new_set.add(element)

        return new_set


    def difference(other_set):
        """Iterate over the two sets and find the elements
        that are not shared and add them to a new set.
        Again trying to decrease overall time complexity by copying the set,
        but the trade off might not be worth it."""

        new_set = Set()

        other_set_copy = other_set

        for element in this.container:
            if not other_set_copy.contains(element):
                new_set.add(element)
            else:
                other_set_copy.remove(element)

        for element in other_set_copy.container:
            if not self.contains(element):
                new_set.add(element)

    def is_subset(other_set):
        """Iterate over the other set and check to see if each element is contained
        in this set. Return False if an element is not found.
        Return True if the entire set has been iterated over.
        Don't iterate over anything if the size of the other_set is larger than this set."""

        if self.size > other_set.size:
            for element in other_set.container:
                if not self.contains(element)
                    return False
            return True
        else:
            return False

# Stretch Challenges
#
# Implement CircularBuffer class (backed by dynamic array) with the following instance methods and properties:
# __init__(max_size) - initialize a new circular buffer that can store at most max_size items
# size - property that tracks the number of items in the buffer
# is_empty - check if the buffer is empty
# is_full - check if the buffer is full
# enqueue(item) - insert item at the back of the buffer
# front - return the item at the front of the buffer
# dequeue - remove and return the item at the front of the buffer
# Annotate enqueue and dequeue methods with running time complexity analysis
# Write unit tests to ensure the CircularBuffer class is robust
# Include test cases for each class instance method and property
# Annotate enqueue and dequeue methods with running time complexity analysis
