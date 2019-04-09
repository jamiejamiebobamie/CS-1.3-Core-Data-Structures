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



# STRETCH CHALLENGE:
# Implement permutation generating functions (try both iterative and recursive versions)
# Implement anagram generating functions (try both iterative and recursive versions)
# Hint: Use the Unix dictionary words list located at: /usr/share/dict/words


string = 'string'

# all permutations of a string
#
# s rtnig
#
# s ntrig
#
# s nirtg
#
# s girtn
#
# s igrtn


def permutation(string):
    def __helper(S, i, result):
        if i < len(S):
            S[0], S[i] = S[i], S[0]
            print(S)
            result.append(S)
            S[0], S[i] = S[i], S[0]
            return __helper(S, i+1,result)
        else:
            return result

    result = []
    string_array = list(string)

    __helper(string_array,0,result)
    return result

string = 'hey'
print(permutation(string))


# wet
# wte

# twe
# tew

# etw
# ewt

def anagram(input_word):
    def makeDictionary():
        f = open("/usr/share/dict/words", "r")
        words = f.read().split()
        f.close()
        return words

    result = []
    words = makeDictionary()
    sorted_input_word = "".join(sorted(input_word))

    for i, word in enumerate(words):
        if "".join(sorted(word)) == sorted_input_word:
            result.append(words[i])
    return result


print(anagram("silence"))

if __name__ == '__main__':
    main()
