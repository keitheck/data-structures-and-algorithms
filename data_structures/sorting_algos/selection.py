def selection_sort(array):
    """
    Sorts an array using a selection sort.
    O(n^2) time, 0(1) space
    """

    if type(array) is not list:
        raise TypeError('Argument must be a list of integers.')

    if len(array) <= 1:
        return array

    for i in range(len(array)):
        """find minimum element in array"""
        temp = array[i]

        for j in range(i, len(array)):
            if array[j] < temp:
                temp = array[j]
                place = j

        if array[i] > array[place]:
            array[i], array[place] = array[place], array[i]    

    return array
