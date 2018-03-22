

def find_index(list, key):
    count = 0
    for index in list:
        if index == key:
            return count
        else:
            count += 1
    return -1

