#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if item == array[index]:
        return index
    elif index < len(array)-1:
        return linear_search_recursive(array, item, index+1)
    else:
        return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests



def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #declare left and right indices
    left, right = 0, len(array)-1

    #initialize while loop, while left is less than or equal to right
    while left <= right:
        #index equals left plus right-left floor-divided by 2.
        #book says this avoids overflow and doesn't have the floor divide. ask in class.
        index = left + (right-left)//2

        #if item is greater than the indexed place in the sorted array
        if array[index] < item:
        #increase the left bound to the index + 1
            left = index + 1
        #if item is at the current currently indexed place in the array
        elif array[index] == item:
        # return the index
            return index
        # else the item is less than the indexed place in the sorted array
        else:
        # decrease upper bound to be one less than the currently indexed place
            right = index - 1
    # if the item is not in the array
    else:
    # return the index that cannot exist in the array
        return -1


def binary_search_recursive(array, item, left=0, right=0,first=True):

        # used to set the 'right' variable
        if first:
            right = len(array)-1
            first = False

        #break if left index grows larger than the right
        #item not found
        if not left <= right:
            return None

        #set the index
        index = left + (right-left)//2

        #if the item at the given index in the array is less than the item searched for
        if array[index] < item:
        #the item is to the right, to the right
            left = index +1
        #if the item at the given index in the array is the item searched for
        elif array[index] == item:
        #return the index
            return index
        #else the item at the given index in the array is greater than the item searched for
        else:
        #the item is to the left, to the left
            right = index -1
        #recurse!
        return binary_search_recursive(array, item, left, right,first)
