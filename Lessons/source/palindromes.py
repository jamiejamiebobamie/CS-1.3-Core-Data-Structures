#!python

import string
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
    # return is_palindrome_recursive(text)

import string
def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here

    #WORKS, but kind of wonky...
#    i = (len(text)-1)//2
#    print(i)
#    while i < len(text):
#        print(i,-i, text[0::i], text[len(text)-1::-i], text[0::i]==text[len(text)-1::-i])
#        if text[0::i]!=text[len(text)-1::-i]:
#            return False
#        i+=1
#    else:
#        return True
    # text = text.lower().translate(string.maketrans(string, string.punctuation))
    # print(text)

    #works if text is pure characters w/o punctuation, whitespace, or change in case
    # i = (len(text)-1)//2
    # print(i, text[0:i], text[len(text):i:-1], len(text) % 2)
    # if len(text) % 2:
    #     return True if text[0:i]==text[len(text):i:-1] else False
    # else:
    #     return True if text[0:i]==text[len(text)-1:i:-1] else False



    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


    if len(text) % 2:
        i = (len(text)-1)//2
        j = (len(text)-1)//2
    else:
        i = (len(text)-1)//2
        j = (len(text)-1)//2+1

    print(i,text[i],j,text[j])

    while i > 0 and j < len(text):
        #if odd amount of numbers:
        if len(text) % 2:
            print(i,text[i],j,text[j])
            if text[i].isalpha():
                if text[j].isalpha():
                    if text[i].lower() == text[j].lower():
                        i, j = i-1, j+1
                    else:
                        return False
                else:
                    j+=1
            else:
                i-=1

        #if even amount of numbers:
        else:
            if text[i].isalpha():
                print(i,text[i],j,text[j])
                if text[j].isalpha():
                    if text[i].lower() == text[j].lower():
                        i, j = i-1, j+1
                    else:
                        return False
                else:
                    j+=1
            else:
                i-=1
    else:
        if text[i].lower() == text[j].lower():
            print(i,text[i],j,text[j])
            return True
        return False

# can't work from the middle. after work from the ends: i = 0 and i = len(text)-1...
print(is_palindrome('!h!!!   o!oh!'))

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


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
