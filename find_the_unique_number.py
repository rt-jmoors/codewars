"""
Description:
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(arr):
    # your code here
    elems = len(arr)
    i = 0
    while i < elems:
        if arr[i] != arr[i + 1]:
            if arr[i] != arr[(i + 2) % elems]:  # wrap around end of arr, when unique element is last in list
                return arr[i]
            else:
                return arr[i + 1]
        i += 1


def find_uniq_better(arr):
    """Better solution"""
    a, b = set(arr)  # Finds unique elements in the list
    return a if arr.count(a) == 1 else b
