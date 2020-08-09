def in_array(array1, array2):
    # your code
    output = []
    for elem1 in array1:
        for elem2 in array2:
            if elem1 in elem2 and elem1 not in output:
                output.append(elem1)
                break # don't want to look for more occurences of elem1 in array2
    output.sort()
    return output