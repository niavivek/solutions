#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports
import re
from string import ascii_letters


# Body
def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_new(words):
    '''Counts the instances of a word in a list and returns a dictionary
    of word counts for each word.
    '''
    d = dict()
    for word in words:
        d[word] = d.get(word, 0) + 1
        # An optional, far clunkier, method may be the following two lines:
        # d.setdefault(word, 0)
        # d[word] += 1
    return d


def get_pledge_list_ascii():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. Returns the list.
    """
    with open('pledge.txt') as f:
        pledge_list = f.read().split()
    # Eliminate punctuation from the end of words with ternary operation
    pledge_list_noPunct = [word if word[-1] in ascii_letters
                           else word[:-1] for word in pledge_list]
    return pledge_list_noPunct


def get_pledge_list_resplit():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. Returns the list.
    """
    pledge_list = []
    with open('pledge.txt') as f:
        # Using a regular expression (or regex) to split on specific end-of-
        # line punctuation chars that are followed by any whitespace
        # characters, but not the hyphen mid-word
        pledge_list = re.split("[\s.:,]\s*", f.read())
    # We must remove the empty string from the end of the list.
    # See: "Why are empty strings returned in split() results?" on
    # StackOverflow.
    pledge_list.pop()
    return pledge_list


def get_pledge_list_resub():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. Returns the list.
    """
    with open("pledge.txt") as f:
        data = f.read()
    data_subed = re.sub("[\s.:,]\s*", " ", data)
    pledge_list = data_subed.split()
    return pledge_list


def get_pledge_list_refindall():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. Returns the list.
    """
    with open("pledge.txt") as f:
        pledge_string = f.read()
    pledge_list = re.findall("\w+", pledge_string)  # splits ever-mindful
    return pledge_list


###############################################################################
def main():  # DO NOT CHANGE BELOW
    print("Using a string.ascii_letters:")
    print(histogram_new(get_pledge_list_ascii()))

    print("\nUsing a re.split():")
    print(histogram_new(get_pledge_list_resplit()))

    print("\nUsing a re.sub():")
    print(histogram_new(get_pledge_list_resub()))

    print("\nUsing a re.findall():")
    print(histogram_new(get_pledge_list_refindall()))

if __name__ == '__main__':
    main()
