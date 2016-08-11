#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports


# Body
def has_no_e(word):
    if "e" not in word:
        return True
    return False


def print_no_e():
    with open("words.txt", "r") as fin:
        lines = fin.readlines()
    count = 0
    for line in lines:
        if has_no_e(line.strip()):
            print(line.strip())
            count += 1
    print("{:.2%}".format(count/len(lines)))


##############################################################################
def main():
    print_no_e()

if __name__ == '__main__':
    main()
