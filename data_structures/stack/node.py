class Node:
    def __init__(self, val, next=None):
        """sets node value upon init"""
        self.val = val
        self._next = next

    def __repr__(self):
        """returns node value"""        
        return self.val

