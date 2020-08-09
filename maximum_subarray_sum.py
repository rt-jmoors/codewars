"""The maximum sum subarray problem consists in finding the maximum sum
    of a contiguous subsequence in an array or list of integers:
"""


def max_sequence(arr):
    if not arr:
        return 0
    i, temp_max = 0, 0
    while i < len(arr):
        if arr[i] < 0:
            i += 1
        for j in range(len(arr), i, -1):
            temp_max = max(temp_max, sum(arr[i:j]))
        i += 1
    return temp_max


