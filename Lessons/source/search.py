#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    print(index)
    # TODO: implement linear search recursively here
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
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #delcare left and right indices
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

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=0, right=0):
    # TODO: implement binary search recursively here
    #initialize while loop, while left is less than or equal to right
        if right == 0:
            right = len(array)-1
        if left > right:
            return None
        index = left + (right-left)//2
        print(item, array[left:right])

        if array[index] < item:
            left = index +1
        elif array[index] == item:
            return index
        else:
            right = index -1

        return binary_search_recursive(array, item, left, right)



    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(binary_search(A, 1))
