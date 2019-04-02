#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    result = 0

    # an array for popping the least significant bit.
    digits_array = list(digits)

    # hex code lookup table.
    lookup = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    # TODO: Decode digits from binary (base 2)
    if base == 2:
        for i, number in enumerate(reversed(digits)):
            result += int(digits_array.pop()) * base**i
        return result

    # TODO: Decode digits from hexadecimal (base 16)
    elif base == 16:
        for i, number in enumerate(reversed(digits)):
            result += lookup[digits_array.pop()]*base**i
        return result

    # TODO: Encode number in any base (2 up to 36)
    else:
        for i, number in enumerate(reversed(digits)):
            if lookup[number] < base:
                result += lookup[digits_array.pop()]*base**i
            else:
                raise IndexError()
        return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    result = 0

    # an array for popping the least significant bit.
    # digits_array = list(number)


    # TODO: Encode digits to binary (base 2)
    if base == 2:
        while number:
            if number % base:
                result +='1'
            else:
                result+="0"
            number = number // base
        return ''.join(reversed(result))

    # TODO: Encode digits to hexadecimal (base 16)
    if base == 16:
        while number:
            result+=number % base
            print(result)
            number = number // base
        return ''.join(reversed(str(result))
        # hex code lookup table.
        # lookup = { '0':'0',  '1':'1',  '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'A', '11':'B', '12': 'C', '13':'D', '14':'E', '15':'F', '10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}
        #
        # array_numbers = list(str(number)) # '100'
        # lookup_index = array_numbers.pop() # '0'
        # test = lookup_index
        # while array_numbers:
        #     while test in lookup:
        #         lookup_index = test
        #         test += array_numbers.pop()
        #         print(test, lookup_index, array_numbers)
        #     else:
        #         result+=lookup[lookup_index]
        #         test = test[-1]
        # else:
        #     result+=lookup[test[-1]]
        # return result


    # TODO: Encode number in any base (2 up to 36)
    # else:
    #     for i, character in enumerate(reversed(number)):
    #         if lookup[number] < base:
    #             result += lookup[digits_array.pop()]*base**i
    #         else:
    #             raise IndexError()
    #     return result

print(encode(100,16))


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
