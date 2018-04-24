

def largest(L):
    """
    function accepts a 2d list of paired ints and returns the largest product of adjacent ints
    """
    # if not input_list:
    #     return 'empty list used'
    # largest_prod = 0
    # product = 0
    # for index in input_list:
    #     product = index[0] * index[1]
    #     if product > largest_prod:
    #         largest_prod = product
    # return largest_prod

    product = 0
    i = 0
    for x in L:
        a = x[i] * x[i + 1]
        if a > product:
            product = a
        b = x[i] * (x + 1)[i]
        if b > product:
            product = b
        c = x[i][1] * x[i + 1][1]
        if c > product:
            product = c
        i += 1
    print('largest product => {}'.format(product))
    return product


test = [[1, 2], [3, 4], [5, 6]]
largest(test)


