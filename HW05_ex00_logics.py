#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_num = input("Enter an integer: ")
    try:
        user_num = int(user_num)
    except ValueError:
        print("{} is not an integer.".format(user_num))
    else:
        if user_num % 2 == 0:
            print("You entered an even number.")
        else:
            print("You entered an odd number.")
    return


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    print("Style #1:")
    for row in range(0, 100, 10):
        for col in range(1, 11):
            print("{:<3}".format(col+row), end="")
        print()

    print("\nStyle #2:")
    for count in range(1, 101):
        print("{:<3}".format(count), end="")
        if count % 10 == 0:
            print()

    print("\nStyle #3:")
    initial_val = 1
    for row in range(0, 10):
        for column in range(0, 10):
            print("{:<3}".format(initial_val), end="")
            initial_val += 1
        print()

    print("\nStyle #4:")
    for x in range(1, 101):
        print("{:<3}".format(x), end="\n" if x % 10 == 0 else "")


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count = 0
    total = 0
    average = 0
    while True:
        user_input = input("> ")
        if user_input == 'done':
            return average
        try:
            total += float(user_input)
        except ValueError:
            print("Sorry. '{}' cannot be cast as float.".format(user_input))
        else:
            count += 1
            average = total/count


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    # even_odd()
    ten_by_ten()
    # print(find_average())


if __name__ == '__main__':
    main()
