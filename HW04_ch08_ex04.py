#!/usr/bin/env python3
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """returns .islower() for the first char only"""
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """(1) returns .islower() for the char "c"
    (2) returns the strings 'True' or 'False' rather than True or False
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """returns only the .islower() from the last char"""
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This works."""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """returns .islower() as soon as it is **not** lower"""
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: print(any_lowercase_("thisstringmessesupthefunction"))
    print(any_lowercase1("Fails"))
    print(any_lowercase2("FAILS"))
    print(any_lowercase3("failS"))
    print(any_lowercase5("faIls"))


if __name__ == '__main__':
    main()
