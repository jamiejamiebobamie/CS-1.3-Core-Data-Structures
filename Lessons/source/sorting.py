#!python



def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.

    Running time: O(n) time complexity unless it breaks early due to being unsorted.
    Memory usage: O(1) space complexity"""
    # TODO: Check that all adjacent items are in order, return early if not

    if not items:
        return True

    i = 0
    while i < len(items)-1:
        if items[i]==min(items[i], items[i+1]):
            i+=1
        else:
            return False
    else:
        return True

# print(is_sorted(A))


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

    Running time: very high, at least O(n). Seeing how many cycles (or loops) of n,
        the runtime was O(81n) (or 81 loops) when the array was in reverse sorted order.

    Memory usage: constant storage or O(1) space complexity."""

    i = 0
    loop = 0

    while not is_sorted(items):
        loop+=1
        # print(loop)
        if i < len(items)-1:
            if items[i] != min(items[i], items[i+1]):
                # print(items[i], items[i+1])
                items[i], items[i+1] = items[i+1], items[i]
            i += 1
        else:
            i = 0
    return items

# print(bubble_sort(B))

import collections

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    minimum = collections.namedtuple("minimum",('index', 'value'))

    first_unsorted_index = 0

    minimum.value = min(items[0], items[1])
    minimum.index = 0
    while not is_sorted(items[:-1]):
        i = 0
        while i < len(items):
            temp_min_value = minimum.value
            minimum.value = min(minimum.value,items[i])
            if temp_min_value != minimum.value:
                minimum.index = i
                # print(minimum.index,minimum.value)
            if i > 0:
                if items[i] < items[i-1]:
                    first_unsorted_index = i-1
            items[minimum.index], items[first_unsorted_index] = items[first_unsorted_index], items[minimum.index]
            print(items)
            i+=1
    return items

C = [10,2,9,1,12,7,3,5,6,8,11,4]
# print(selection_sort(C))

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items



    # iterate through the array with i.
    # find the first unsorted item.
    #
    # put that item at the beginning of the array.
    # that first element is the start of a subarray from 0 to j.
    #
    # increase j by one.
    # find the next unsorted item and put it in the subarray by comparing all the items
    # in the subarray.
    #
    # once the subarray item being compared to the unsorted item is bigger than the unsorted item,
    # insert the item with at that index k , .insert(k,item).

    j = 0

    while j <= len(items):

        i = 0
        while i < len(items)-1:

            if items[i] > items[i+1]:
                j+=1
                temp = items[i]
                del items[i]

                k = 0
                while k < j:
                    print(temp,k,items)
                    if items[k] > temp:
                        items.insert(k, temp)
                    k+=1
                else:
                    items.insert(k, temp)
            i+=1

    temp = items.pop()
    i = 0
    while items[i] < temp:
        i+=1
    else:
        items.insert(i, temp)


    return items


A = [0,1,1,2,5,6,7,8,9,10,11,15,20]
B = [-1,-1,0,0,1,2,3,4,5,6,10,11,11,11,11,11,11]

C = [10,2,9,1,12,7,3,5,6,8,11,4]

D = [10,9,3,4,8,9,345,2,12,1]

print(insertion_sort(C))


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    Running time: O(m+n), where m is the size of items1 and n is the size of items2.

    Memory usage: O(m+n): the combined size of the two lists."""

    mergedList = [None]*len(items1)+[None]*len(items2)

    mergedList_index = len(mergedList)-1

    while items1 and items2:
        if items1[len(items1)-1] >= items2[len(items2)-1]:
            mergedList[mergedList_index] = items1.pop()
        else:
            mergedList[mergedList_index] = items2.pop()
        mergedList_index -= 1
    else:
        while items1:
            mergedList[mergedList_index] = items1.pop()
            mergedList_index -= 1
        while items2:
            mergedList[mergedList_index] = items2.pop()
            mergedList_index -= 1

    return mergedList



# print('merged',merge(A, B))

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    partition = len(items)//2
    return merge(bubble_sort(items[:partition]),bubble_sort(items[partition:]))

# print(split_sort_merge(C))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    partition = len(items)//2
    # return merge(items[:partition],items[partition:])

    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

# print(merge_sort(C))

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) under all conditions
    Memory usage: O(n) under all conditions

    Pivot chosen by finding the median between the low and high bounds.
    """

    #"the dutch national flag problem"

    if high > len(items)-1:
        raise ValueError("You're array only goes to {}.".format(len(items)-1))
    if low < 0:
        raise ValueError("An array starts at index 0.")

    pivot_index = (high - low) // 2

    value = items[pivot_index]

    smaller = []
    equal = []
    larger = []

    for _ in range(len(items[low:high+1])):
        if items[_] < value:
            smaller.append(items[_])
        elif items[_] == value:
            equal.append(items[_])
        else:
            larger.append(items[_])
    return smaller + equal + larger

# print(partition(D, 2, 9))


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.

    Running time: O(n+(m-l)) with n being the size of the array,
        and m-l being the range between the maximum and the minimum numbers.

    Memory usage: O(1)"""

    result = []

    maximum = float('-inf')
    minimum = float('inf')

    dict = {}
    for num in numbers:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    # for _ in range(minimum, maximum+1):
    #     if dict[_]:
    #         result+=[_]*dict[_]

    # FIXME FIX:
    i = 0
    for _ in range(minimum, maximum+1):
        if dict[_]:
            for j in range(dict[_]):
                numbers[i] = _
                i+=1

    # return result
    return numbers


E = [1,2,3,4,5,6,6,1,7,3,8,9,9,9,9,9,10]
# print(counting_sort(E))

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
