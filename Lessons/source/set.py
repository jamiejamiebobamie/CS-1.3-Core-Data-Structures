# Implement Set class (abstract data type backed by data structure of your choice) with the following
# set operations as instance methods and properties:
# __init__(elements=None) - initialize a new empty set structure, and add each element if a sequence is given
# size - property that tracks the number of elements in constant time
# contains(element) - return a boolean indicating whether element is in this set
# add(element) - add element to this set, if not present already
# remove(element) - remove element from this set, if present, or else raise KeyError
# union(other_set) - return a new set that is the union of this set and other_set
# intersection(other_set) - return a new set that is the intersection of this set and other_set
# difference(other_set) - return a new set that is the difference of this set and other_set
# is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set
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

        new_set = Set()




    def intersection(other_set):
    """Iterate through the smaller set and the items contained
            in both sets to a new set."""

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

        - return a new set that is the intersection of this set and other_set
    def difference(other_set) - return a new set that is the difference of this set and other_set
    def is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set



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
