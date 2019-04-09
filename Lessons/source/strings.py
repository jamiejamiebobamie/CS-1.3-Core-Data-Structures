#!python

import collections

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    i = len(pattern)
    if i < 1:
        return True
    target = collections.deque(list(pattern))
    deck = collections.deque(text[:i])

    while i < len(text):
        if deck == target:
            return True
        deck.popleft()
        deck.append(text[i])
        i+=1
    else:
        if deck == target:
            return True
        return False

    # TODO: Implement contains here (iteratively and/or recursively)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Time Complexity:
        O(n) at worst if the pattern is not in the text
        or if the pattern is at the very end
        At best O(m), if the pattern is the first characters of the text.

    Space Complexity:
        O(2m), the deque which is the size of the pattern, doubled.

    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    i = len(pattern)
    if i < 1:
        return 0
    target = collections.deque(list(pattern))
    deck = collections.deque(text[:i])

    while i < len(text):
        if deck == target:
            return i-len(target)
        deck.popleft()
        deck.append(text[i])
        i+=1
    else:
        if deck == target:
            return i-len(target)
        return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    i = len(pattern)
    if i < 1:
        return list(range(len(list(text))))
    target = collections.deque(list(pattern))
    deck = collections.deque(text[:i])
    indices = []

    while i < len(text):
        if deck == target:
            indices.append(i-len(target))
        deck.popleft()
        deck.append(text[i])
        i+=1
    else:
        #in case the last letters in the deck match the pattern:
        if deck == target:
            indices.append(i-len(target))
        #return the indices
        return indices


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
