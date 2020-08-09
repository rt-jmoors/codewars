"""
Description:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    # your code here
    zeroes = [x for x in array if x == 0 and x is not False]
    non_zeroes = [x for x in array if x != 0 or x is False]
    return non_zeroes + zeroes


def kata_move_zeros(arr):
    # only extracts values that aren't 0, or are Boolean values (to keep the 'False' values)
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    # returns everything removed, and appends a list of 0's to match the missing amounts removed
    return l + [0] * (len(arr) - len(l))


move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])  # should return [False,1,1,2,1,3,"a",0,0]

