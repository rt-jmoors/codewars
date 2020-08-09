def zeros(n):
    n = 10
    product = 1
    while n > 0:
        product *= n
        n -= 1

    result = str(product)[::-1]
    counter = 0
    for digit in result:
        if int(digit) == 0:
            counter += 1
        else:
            break
    return counter
