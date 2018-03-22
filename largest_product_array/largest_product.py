

def largest(input_list):
    """
    function accepts a 2d list of paired ints and returns the largest product of adjacent ints
    """
    if not input_list:
        return 'empty list used'
    largest_prod = 0
    product = 0
    for index in input_list:
        product = index[0] * index[1]
        if product > largest_prod:
            largest_prod = product
    return largest_prod

