"""
node.py sets up the head and node, and metadata that links list noes
"""


class Node:

    def __init__(self, val, next=None):
        """
        set up __init__ function that sets the value to next to None (sets as last node)
        """
        self.val = val
        self._next = next  # this will update to the location of the next node when next node created

    def __str__(self):
        """
        this is a special method that we can define to represent an output value for an instantiated object
        """
        return '{val}'.format(val=self.val)


