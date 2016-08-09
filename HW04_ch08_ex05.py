#!/usr/bin/env python3
# HW04_ch08_ex05
# This is based on thisisedyip's assignment.


def rotate_letter(letter, n):
    """Identify start, original letter, add integer to normalized value, `% 26`
    to ensure ord value doesn't go over or under alphabet scale, convert back
    to assigned letter
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')

    letter_ord = ord(letter) - start
    new = (letter_ord + n) % 26 + start

    return chr(new)


def rotate_word(word, n):
    """Initialize newword to concatenate onto, for each letter in word call
    rotate_letter, add returned changed letter one at a time
    """
    newword = ''    #
    for letter in word:     #
        newword = newword+rotate_letter(letter, n)
    return newword


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(f, s, n, expected):
    if f(s, n) == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{:<1} {:<7} by {:<4}=> got: {:<7} expected: {}'.format(
                prefix,
                repr(s),
                repr(n),
                repr(f(s, n)),
                repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('rotate_word')
    print('Book Examples:')
    test(rotate_word, 'A', 3, 'D')
    test(rotate_word, 'Z', 1, 'A')
    test(rotate_word, 'cheer', 7, 'jolly')
    test(rotate_word, 'melon', -10, 'cubed')
    test(rotate_word, 'IBM', -1, 'HAL')
    print('\nDaniel\'s Tests:')
    test(rotate_word, 'abc', 1, 'bcd')
    test(rotate_word, 'xyz', 1, 'yza')
    test(rotate_word, 'ABC', 1, 'BCD')
    test(rotate_word, 'XYZ', 1, 'YZA')
    test(rotate_word, 'Az', 1, 'Ba')
    test(rotate_word, 'Aa', 26, 'Aa')
    test(rotate_word, 'abc', -1, 'zab')
    test(rotate_word, 'xyz', -1, 'wxy')
    test(rotate_word, 'ABC', -1, 'ZAB')
    test(rotate_word, 'XYZ', -1, 'WXY')
    test(rotate_word, 'Az', -1, 'Zy')
    test(rotate_word, 'Aa', -26, 'Aa')
main()