from .node import Node


class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        """"""
        # return '<BST Root => {}>'.format(self.root.val)
        return '<leaf vals => root: {} | Left: {} | Right: {}'.format(self.root.val, self.root.left.val, self.root.right.val)

    def __str__(self):
        """returns the root val of BST"""
        return 'root. val => {}'.format(self.root.val)

    def in_order_traversal(self, operation=None):
        """search function that traverses bst in order | go left, look at node, go right"""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)
         
            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order_traversal(self, operation=None):
        """look at node, go left, go right"""    
        def _walk(node=None):
            if node is None:
                    return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)
        
        _walk(self.root)

    def post_order_traversal(self, operation=None):
        """go left, go right, then look at node"""
        def _walk(node=None):
            if node is None:
                    return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)
        
            operation(node)

        _walk(self.root)

    def insert(self, val):
        """insert adds a value to the binary search tree in a sorted order"""
        if not (type(val) is float or type(val) is int):
            raise TypeError('val must be and int or float') 

        node = Node(val) 
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break
   
            if val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node


# def _filler():
#     """helper function that fills list with random ints"""
#     from random import randint
#     ls = [randint(0, 1000) for num in range(20)]
#     # a.insert(ls)
#     for num in ls:
#         a.insert(num)