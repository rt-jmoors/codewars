"""
You will be given a number and you will need to return it as a
string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""


def expanded_form(num):
    # reverse num as string for enumeration
    num_s = str(num)[::-1]
    # use enumeration of reversed digits in num to calculate number of zeroes to append
    output = [digit + num_zeroes*'0' for num_zeroes, digit in enumerate(num_s) if digit != '0']
    # undo initial reversing of num as string
    return ' + '.join(reversed(output))


