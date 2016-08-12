#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports


# Body
def is_abecedarian(word):
    return sorted(list(word)) == list(word)


def bulk_abecedarian_checker(file_name):
    abecedarian_word_count = 0
    with open(file_name, "r") as fin:
        for line in fin.readlines():
            if is_abecedarian(line.strip()):
                abecedarian_word_count += 1
    return abecedarian_word_count


##############################################################################
def main():
    print(is_abecedarian("zyx"))
    print(is_abecedarian("abc"))
    print(bulk_abecedarian_checker("words.txt"))

if __name__ == '__main__':
    main()
