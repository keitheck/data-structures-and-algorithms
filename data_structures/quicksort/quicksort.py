def quicksort(array):
    """
    Returns an ordered list using a quicksort algorithm.
    """

    if len(array) == 1 or len(array) == 0:
        return array

    piv = array[len(array) - 1]
    R, L, P = [], [], []

    while array[0] != piv:
        if array[0] > piv:
            R.append(array.pop(0))
        elif array[0] < piv:
            L.append(array.pop(0))
    P = [piv]

    return quicksort(L) + P + quicksort(R)
