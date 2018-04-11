def recursive_function(n):
    """this function is me trying to understand recurtion"""
    x = []
    while n > 0:
        x.append(n)
        n -= 1
        recursive_function(n)
    return x  


def tower(n, a, b, c):
    """this is a recursive solution to the tower of hanoi.  Using the visual() function to print steps to terminal so I user cab understand the process"""
    if n == 0:
        return "empty, not moves possible"
    else:
        """call itself"""
        tower(n-1, a, c, b)
        visual(n, a, b)
        tower(n-1, c, b, a)
    return z


z = []


def visual(num, movefrom, moveto):
    y = (num, "from", movefrom, "to", moveto)
    z.append(str(y)) 

"""
suggested calls to illustrate recursive solution to towers of hanoi:
tower(2, "a", "b", "c")
tower(3, "a", "b", "c")
"""
