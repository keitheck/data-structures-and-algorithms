from .node import Node


class Stack:

    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        self.is_awesome = True

        if type(iterable) is dict:
            for key,value in dict.items():
                self.push({key:value})
        
        try:
            for item in reversed(iterable):
                self.push(item)
        except TypeError:
            print('please instansiate with an iterable')
    
    def __len__(self):
        """returns the length (height?) of the stack"""
        return self._size

    def __str__(self):
        """custom str, returns a string interp of stack"""
        t = 'top'
        i = self.top
        while i:
            t = t + ' {} =>'.format(i.val)
            i = i._next
        return t

    def __is_awesome__(self):
        return self.is_awesome

    def push(self, val):
        """adds a node to top of stack"""
        node = Node(val, self.top)
        node._next = self.top
        self.top = node
        self._size += 1
        return self.top

    popval = None

    def pop(self):
        """removes the top value and returns the value"""
        if self is None:
            return False
        node = self.top
        self.top = node._next
        self._size -= 1
        return node.val
            
    def peek(self):
        if self is None:
            return False
        return self.top.val

    

       
