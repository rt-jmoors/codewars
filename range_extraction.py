def solution(args, min_length=3):
    """
    Description:
    A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
    Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

    Example:

    solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    # returns "-6,-3-1,3-5,7-11,14,15,17-20"
    :param args:
    :param min_length: min length for continuous numbers where a '-' will be inserted
    :return:
    """
    args.sort()
    if min_length <= 1 or len(args) < min_length:
        return ','.join([str(x) for x in args])

    # calculate all lengths of continuous numbers
    lengths = []
    length = 1
    for i in range(0, len(args) - 1):
        if args[i + 1] == args[i] + 1:
            length += 1
        else:
            lengths.append(length)
            length = 1
    # need to capture the last length
    lengths.append(length)
    print(lengths)

    # format output
    index = 0
    output = []
    for length in lengths:
        if length < min_length:
            output.extend(args[index:index + length])
        else:
            output.append(str(args[index]) + '-' + str(args[index + length - 1]))
        index += length

    return ','.join([str(x) for x in output])


def kata_solution(args):
    # really clever solution, similar to mine but probably faster
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


args = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
kata_solution(args)
