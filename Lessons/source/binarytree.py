#!python

import collections


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left == None and self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.left != None or self.right != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Running time:
        Best: O(h) or O(log(n)).
        Worst: O(n) if you have a left or right skewed tree."""

        height = -1

        def __helper(node, height):
            if node:
                height+=1
                return max(__helper(node.left, height), __helper(node.right, height))
            return height

        return __helper(self, height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Running time:
        Best: O(h) or O(log(n)).
        Worst: O(n) if you have a left or right skewed tree."""

        height = -1

        def __helper(node, height):
            if node:
                height+=1
                return max(__helper(node.left, height), __helper(node.right, height))
            return height

        return __helper(self.root, height) if not self.is_empty() else 0

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(logn) if normal tree
        Worst case running time: O(n) if skewed"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(logn) if normal tree
        Worst case running time: O(n) if skewed"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(logn) if normal tree
        Worst case running time: O(n) if skewed"""
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size +=1
            return

        parent = self._find_parent_node_recursive(item, self.root)

        if parent and parent.data > item:
            parent.left = BinaryTreeNode(item)
        elif parent and parent.data < item:
            parent.right = BinaryTreeNode(item)
        self.size +=1


    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(logn) if normal tree
        Worst case running time: O(n) if skewed"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(logn) if normal tree
        Worst case running time: O(n) if skewed"""
        if node is None:
            return None
        if node.data == item:
            return node
        elif item < node.data:
            return self._find_node_recursive(item, node.left)
        elif item > node.data:
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(logn) if normal tree
        Worst case running time: O(n) if skewed"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""

        if parent == None:
            parent = self.root

        if node is None:
# Not found (base case) #SUPPOSE TO RETURN NONE...
            return parent

        # Check if the given item matches the node's data
        if item == node.data:
            # print("the true true")
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node) # Hint: Remember to update the parent parameter
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)  # Hint: Remember to update the parent parameter

    def delete(self, item):
        # BROKEN
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        def __helper():
            left = 1
            if node.data == item and left:
                parent.left = None
                return True
            elif item < node.data:
                if left:
                    pass
                else:
                    left^=left
                parent = node
                node = node.left
            elif item > node.data:
                if left:
                    left^=left
                else:
                    pass
                parent = node
                node = node.right
        return __helper()

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items)#.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        if node:
            self._traverse_in_order_recursive(node.left, visit)
            visit.append(node.data)
            self._traverse_in_order_recursive(node.right, visit)
        return


    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        parent = node
        while node.left and parent:
            parent = node
            node = node.left
        else:
            visit.append(parent.left.data)

        # TODO: Traverse in-order without using recursion (stretch challenge)


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        if node:
            # print(node.data)
            visit.append(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
            self._traverse_pre_order_recursive(node.right, visit)
        return

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        # Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        if node:
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit.append(node.data)
        return

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Best and worst case run time: O(n) at most you're traversing a node once."""

        queue = collections.deque() # don't need a double-ended queue.
        queue.append(start_node)

        while len(queue):
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                visit.append(node.data)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]



# insert(4), size: 0
# insert(2), size: 1
# (2, 'PARENT:', 4, 'LEFT:', BinaryTreeNode(2), 'RIGHT:', None)
# insert(6), size: 2
# (6, 'PARENT:', 4, 'LEFT:', BinaryTreeNode(2), 'RIGHT:', BinaryTreeNode(6))
# insert(1), size: 3
# (1, 'PARENT:', 2, 'LEFT:', BinaryTreeNode(1), 'RIGHT:', None)
# insert(3), size: 4
# (3, 'PARENT:', 2, 'LEFT:', BinaryTreeNode(1), 'RIGHT:', BinaryTreeNode(3))
# insert(5), size: 5
# (5, 'PARENT:', 6, 'LEFT:', BinaryTreeNode(5), 'RIGHT:', None)
# insert(7), size: 6
# (7, 'PARENT:', 6, 'LEFT:', BinaryTreeNode(5), 'RIGHT:', BinaryTreeNode(7))

#                            4
#                2                       6
#            1       3               5       7


#________________________________________________________________

    #                4
    #        2               6
    #    1       3       5       7

    # if node:
    #     visit.append(node.data)
    #     self._traverse_in_order_recursive(node.left, visit)
    #     self._traverse_in_order_recursive(node.right, visit)
    # return

    # my code: items pre-order:   [4, 1, 2, 3, 5, 6, 7]
    # assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]

    # items pre-order:   [4, 1, 2, 3, 5, 6, 7]

    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        print('insert({}), size: {}'.format(item, tree.size))
        tree.insert(item)
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
