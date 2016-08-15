#!/usr/bin/env python3
# HW07_ch10_ex03

# Instructions:
# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3, 4] is [1, 3, 6, 10]
#  - in the above example I want returned the list: [1, 3, 6, 10]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################################
# Imports


# Body
def cumulative_sum(lst):
    cumulative_sum_lst = [lst[0]]
    for idx, item in enumerate(lst[1:]):
        cumulative_sum_lst.append(item+cumulative_sum_lst[idx])
    return cumulative_sum_lst


##############################################################################
def main():
    print(cumulative_sum([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()
