def radix_sort(arr):
    """
    Takes a list of positive unordered integers and returns an
    ascending sorted list using radix_sort.
    """
    if type(arr) is not list:
        return TypeError('Must use a list of positive integers.')

    for item in arr:
        if item < 0:
            return TypeError('Must not contain negative integers.')   

    iteration = 0  # used to select digit place
   
    while iteration <= len(str(max(arr))):
        presort = array_buckets(arr, iteration)
        arr = sorted_list(presort)
        iteration += 1

    return arr


def place_value(num, iteration):
    """helper that returns diget in given place"""
    return (num // (10 ** iteration)) % 10


def array_buckets(array, iteration):
    """helper that sorts array into buckes based on iteraton"""
    # buckets = [[] for L in 10]
    buckets = [[], [], [], [], [], [], [], [], [], []]
    for item in array:
        buckets[place_value(item, iteration)].append(item)
    return buckets


def sorted_list(buckets):
    """Sorts buckets to list"""
    output = []
    for bucket in buckets:
        for item in bucket:
            output.append(item)
    return output
