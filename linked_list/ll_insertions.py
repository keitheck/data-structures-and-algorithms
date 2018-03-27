from node import Node
from linked_list import LinkedList 


class ll_methods(LinkedList):
    """
    the class inherits from LinkedList
    """
    def append(self, val):
        """add node to end of LL"""
        node_index = self.head
        if not node_index._next:
            node_index = Node(val)

        while node_index._next:
            node_index = node_index._next

        node_index._next = Node(val)        

    def insertBefore(self, val, newVal):
        """add node with new Val before node with val"""
        pass

    def insertAfter(self, val, newVal):
        """add node with new val after node with val"""
        pass     