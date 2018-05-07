def mergesort(arr):
    """
    A recursive function that accepts an array of unsorted integers and
    returns a sorted array
    """
    if type(arr) is not list:
        raise TypeError('argument must be list of integers')

    if len(arr) <= 1:
        return arr    

    def recurse(arr):
        half = len(arr)//2
        left = []
        right = []

        for i in range(half):
            left = left + [arr[i]]
            right = right + [arr[len(arr) - 1 - i]]
        print('split', left, right)
        if len(left) > 1:
            left = recurse(left)
        if len(right) > 1:
            right = recurse(right)
        
        return merge(left, right)    
        
    def merge(left, right):
        output = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                output.append(left[i])
                i = i + 1
            elif left[i] >= right[j]:
                output.append(right[j])
                j = j + 1
            print('merging', left, right, '=>', output)
        output.extend(left[i:])
        output.extend(right[j:])


        print('merged', output, '\n')
        return output

    return recurse(arr)
   