#!python

import string
ALPHA = frozenset(string.ascii_letters)
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text,0,len(text)-1)

def is_palindrome_iterative(text):

    left = 0
    right = len(text)-1

    while left < right:
        #check if the left and right items are alpha characters:
        if text[left] in ALPHA:
            if text[right] in ALPHA:

                #if they both are alpha characters check to see if they are the same character,
                    #and increment the indices by one to go towards the center:
                if text[left].lower() == text[right].lower():
                    left, right = left+1, right-1

                #not a pallindrome:
                else:
                    return False
            #right item is not alpha:
            else:
                right-=1
        #left item is not alpha:
        else:
            left+=1
    #the left index is greater than the right, and all characters iterated through are equal,
    #return True, it's a pallindrome
    else:
        return True

def is_palindrome_recursive(text, left=None, right=None):

    if left < right:
        if text[left] in ALPHA:
            if text[right] in ALPHA:
                if text[left].lower() == text[right].lower():
                    return is_palindrome_recursive(text, left+1, right-1)
                else:
                    return False
            else:
                return is_palindrome_recursive(text, left, right-1)
        else:
            return is_palindrome_recursive(text, left+1, right)
    else:
        return True



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
