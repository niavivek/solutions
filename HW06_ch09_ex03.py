#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import string
import itertools

# Body


def avoids(word, forbidden_string):
    """ return True if word NOT forbidden"""
    for char in forbidden_string:
        if char in word:
            return False
    return True


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    forbidden_string = input(">")
    count_clean = 0
    with open("words.txt", "r") as f:
        for word in f:
            if avoids(word, forbidden_string):
                count_clean += 1
    print(count_clean)


def forbidden_param(words, forbidden_string):
    """ return count of words NOT forbidden by param"""
    count_clean = 0
    for word in words:
        if avoids(word, forbidden_string):
            count_clean += 1
    return count_clean


def find_five():
    count_clean = 0
    excludes_smallest = []
    with open("words.txt", "r") as f:
        words = f.readlines()  # 113809
    combos = list(itertools.combinations(string.ascii_lowercase, 5))  # 65780
    for each in combos:
        # Count of words not forbidden by letters
        tmp_clean = forbidden_param(words, each)
        # If last check than previous best: update count & letters
        if tmp_clean > count_clean:
            count_clean = tmp_clean
            excludes_smallest = each
    print(count_clean, excludes_smallest)


##############################################################################
def main():
    # forbidden_prompt()
    find_five()  # 96425 ('j', 'q', 'w', 'x', 'z')

if __name__ == '__main__':
    main()
