#!python

import string



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

    for i, number in enumerate(reversed(digits)):
        result += lookup[digits_array.pop()]*base**i
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

    result = ''

    number = int(number)

    lookup = { '0':'0',  '1':'1',  '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'A', '11':'B', '12': 'C', '13':'D', '14':'E', '15':'F', '10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f', '16':'g', '17':'h', '18':'i', '19':'j', '20':'k', '21':'l', '22':'m', '23':'n', '24':'o', '25':'p', '26':'q', '27':'r', '28':'s', '29':'t', '30':'u', '31':'v', '32':'w', '33':'x', '34':'y', '35':'z'}

    while number:
        remainder = number % base
        result+=str(lookup[str(remainder)])
        number = number // base
    return ''.join(reversed(str(result)))


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    if base1 == 2 and base2 == 10:
        return str(decode(digits, base1))

    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    elif base1 == 10 and base2 == 16:
        return str(encode(digits, base2))

    # TODO: Convert digits from any base to any base (2 up to 36)
    else:
        return str(encode(decode(digits, base1), base2))


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
