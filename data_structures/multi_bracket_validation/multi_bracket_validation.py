from .stack import Stack

pile = Stack()


def switch(bracket):
    """returns the closing bracket"""
    if bracket == '(':
        return ')'

    if bracket == '{':
        return '}'

    if bracket == '[':
        return ']'


def multi_bracket_validation(string):
    """returns a boolean True if brackets in string are balanced"""
    print('ran')
    # try:
    # import pdb; pdb.set_trace()
    for char in string:
        print('input', char)
        if char in '({[':
            print('pushed => ', char)
            pile.push(switch(char))
        
        if char in ')}]':
            if pile.top is None:
                return False
            if pile.top.val == char:
                print('pile pop val', pile.top.val)
                pile.pop()   
    
    if pile.top is None:
        return True
    else:
        return False
    # except TypeError:
    #     Print('error')



