#!/usr/bin/env python3
# HW08_ch11_ex02d.py

# Instructions:
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Notes:
#   - There are two examples for new ways of inverting a dictionary, see
#     explanations where code is used:
#       - .setdefault
#       - .defaultdict
#   - Depending on which you use, you will have to print differently as well.
#   - One version demonstrates how sorted might be done when the inverted
#     dictionary is created so that the values are printed alphabetized.
###############################################################################
# Imports
from collections import defaultdict
from string import ascii_letters


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new_setdefault_style(d):
    inverse = {}
    for key, val in d.items():
        # .setdefault syntax is .setdefault(key, default)
        # If key is in the dictionary (inverse), setdefault returns its value.
        # If not, it inserts the key with a value of the default and returns
        # the default. Then .append is invoked on val/default and appends the
        # key.
        inverse.setdefault(val, []).append(key)
    return inverse


def invert_dict_new_defaultdict_style(d):
    # For reference on defaultdict see collections.defaultdict (docs 8.3.3)
    # If default_factory (the first param in defaultdict is not None, it is
    # called without arguments to provide a default value for the given key,
    # this value is inserted in the dictionary for the key, and returned.
    inverse = defaultdict(list)
    # Demonstrating another possibility: you can loop through a sorted list
    # of the keys so that the values of the inverted dict appear in
    # alphabetical order.
    for key in sorted(d.keys(), key=str.lower):
        inverse[d[key]].append(key)
    return inverse


def print_hist_newest_setdefault_style(d):
    for key in range(1, max(d.keys())+1):
        if key in d:
            print("{key}: {vals}".format(key=key, vals=d[key]))
        else:
            print("{key}: ".format(key=key))


def print_hist_newest_defaultdict_style(d):
    for key in range(1, max(d.keys())+1):
        # When d is checked for key, if the key is not there it is added and
        # initialized by whatever function created the defaultdict, here list.
        if len(d[key]) > 0:
            print("{key}: {vals}".format(key=key, vals=d[key]))
        else:
            print("{key}: ".format(key=key))


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_new(list_):
    '''Counts the instances of a word in a list and returns a dictionary
    of word counts for each word.
    '''
    d = dict()
    for word in list_:
        d[word] = d.get(word, 0) + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt') as f:
        pledge_list = f.read().split()
    # Eliminate punctuation from the end of words with ternary operation
    pledge_list_noPunct = [word if word[-1] in ascii_letters
                           else word[:-1] for word in pledge_list]
    return pledge_list_noPunct


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a ABOVE: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW

    pledge_histogram = histogram_new(get_pledge_list())

    # Using .setdefault in the setdefault_style functions:
    print("Using .setdefault:")
    pledge_invert = invert_dict_new_setdefault_style(pledge_histogram)
    print_hist_newest_setdefault_style(pledge_invert)

    # Using .defaultdict in the defaultdict_style functions:
    print("\nUsing .defaultdict (and sorted(d.keys(), key=str.lower):")
    pledge_invert = invert_dict_new_defaultdict_style(pledge_histogram)
    # Note that defaultdict is a subclass of the built-in dict class - check
    # this by running the below line:
    # print(type(pledge_invert))
    # Note the only method changed in defaultdict is how __getitem__() works.
    # Checking for a key in a defaultdict, if it isn't there, adds the key
    # to the dictionary with the default_factory (which is build into the
    # defaultdict when it was created.) See this by uncommenting the line
    # below and the line immediately after print_hist_newest_defaultdict_style
    # is called. You will note the 4 and 8 are not keys at first, but is added
    # when checked by our printing function.
    # print("\nlength: {0}\n{1}\n".format(len(pledge_invert), pledge_invert))
    print_hist_newest_defaultdict_style(pledge_invert)
    # print("\nlength: {0}\n{1}\n".format(len(pledge_invert), pledge_invert))

if __name__ == '__main__':
    main()