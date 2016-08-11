#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports


# Body
def uses_all(word, req_letters):
    for letter in req_letters:
        if letter not in word:
            return False
    return True


def contains_all_required_letters(req_letters):
    count = 0
    with open("words.txt", "r") as fin:
        words_list = fin.readlines()
    for line in words_list:
        word = line.strip()
        if uses_all(word, req_letters):
            count += 1
    print("There are {} words containing all letters in '{}'".format(
        count, req_letters))


##############################################################################
def main():
    contains_all_required_letters("aeiou")
    contains_all_required_letters("aeiouy")


if __name__ == '__main__':
    main()