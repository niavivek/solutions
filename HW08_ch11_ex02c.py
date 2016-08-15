#!/usr/bin/env python3
# HW08_ch11_ex02c.py

# Instructions:
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Notes:
#   - This presents two ways of writing reverse_lookup_new:
#       - list comprehension
#       - for loop
###############################################################################
# Imports
from string import ascii_letters

# Body


def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new_listcomprehension(d, v):
    matches = [k for k in d if d[k] == v]
    return matches


def reverse_lookup_new_forloop(d, v):
    matches = list()
    for k in d:
        if d[k] == v:
            matches.append(k)
    return matches


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_new(words):
    '''Counts the instances of a word in a list and returns a dictionary
    of word counts for each word.
    '''
    d = dict()
    for word in words:
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
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())

    print("Using a list comprehension:")
    print(reverse_lookup_new_listcomprehension(pledge_histogram, 1))
    print(reverse_lookup_new_listcomprehension(pledge_histogram, 9))
    print(reverse_lookup_new_listcomprehension(pledge_histogram, "Python"))

    print("\nUsing a for loop:")
    print(reverse_lookup_new_forloop(pledge_histogram, 1))
    print(reverse_lookup_new_forloop(pledge_histogram, 9))
    print(reverse_lookup_new_forloop(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
