

def find_index(list, key):
    """
    This function accepts a sorted list of ints of unknown length and
    a key value.  Will return the index of matched key.
    """
    count = 0
    for index in list:
        if index == key:
            return count
        else:
            count += 1
    return -1

