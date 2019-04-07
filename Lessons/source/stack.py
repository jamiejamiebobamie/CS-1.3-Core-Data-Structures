#!python

from linkedlist import LinkedList, Node


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        self.next_tail = None
        if iterable is not None:
            for item in iterable:
                # print(item,)
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.size == 0
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size
        # TODO: Count number of items

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        self.list.append(item)
        return True

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        #NOTE: pop() method DOES NOT  reassign self.list.tail to None if last item is popped and the list is empty...
        return self.list.tail.data if not self.is_empty() else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        pass
        Running time: O(???) – Why? [TODO]"""
        # print(self.list.is_empty(), self.list.size)
        if not self.is_empty():
            node = self.list.tail
            # print('node', node)
            if self.list.tail.last:
                self.list.tail = self.list.tail.last
            # else:
            #     self.list.tail = None
            if self.list.tail.next:
                self.list.tail.next = None
            self.list.size -= 1
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
            print(str(iterable))
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
        Running time: O(???) – Why? [TODO]"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        return self.list[self.length()-1] if self.length() else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.list:
            return self.list.pop(self.length()-1)
        else:
            raise ValueError('Empty list.')


#Implement LinkedStack and ArrayStack above, then change the assignment below
#to use each of your Stack implementations to verify they each pass all tests


# Stack = LinkedStack
Stack = ArrayStack
