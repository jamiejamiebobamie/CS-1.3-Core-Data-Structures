#!python

from linkedlist import LinkedList, Node

class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        self.list = LinkedList()
        self.next_tail = None
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.size == 0

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1), you're adding to the tail of the list and then
        reassigning the tail to the new node. all constant time operations."""
        self.list.append(item)
        return True

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        return self.list.tail.data if not self.is_empty() else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        pass
        Running time: O(1), the list contains a pointer to the tail
        and the tail contains a pointer to the second to last node."""
        if not self.is_empty():
            node = self.list.tail
            if self.list.tail.last:
                self.list.tail = self.list.tail.last
            if self.list.tail.next:
                self.list.tail.next = None
            self.list.size -= 1
            if self.is_empty():
                self.list.head =self.list.tail = None
            return node.data
        else:
            raise ValueError("Stack is empty.")


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return not self.list

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1), you're adding to the top of the stack"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        return self.list[self.length()-1] if self.length() else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1), you're removing from the top of the stack"""
        if self.list:
            return self.list.pop(self.length()-1)
        else:
            raise ValueError('Empty list.')


#Implement LinkedStack and ArrayStack above, then change the assignment below
#to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
