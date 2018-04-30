def repeated_word(val):
    """
    finds the first instance of a repeated word in a string and returns the value of that word as a string
    """

    if type(val) is not str:
        raise TypeError

    val = val.lower() + ' '
    words = []
    word = ''
    
    for letter in val:
        if letter == ' ':
            words = words + [word]
            word = ''
        else:
            word = word + letter
    
    arr = []

    for item in words:
        
        if item not in arr:
            arr = arr + [item]
        else:
            return item
    
    return 'No duplicate words found'