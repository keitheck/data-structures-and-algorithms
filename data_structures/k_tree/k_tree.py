class Node:
    """defines each node used to build the k-ary tree"""
    def __init__(self, val, input_list=[]):
        self.val = val
        self.children = []
        for child in input_list:
            self.children.append(Node(child))

    def __repr__(self):
        # return 'node children: {} '.format(lambda x: for x in self.children: return x.val)
        return str(self.val) 

    def __str__(self):
        return 'node value: {}'.format(self.val)


class Ktree:
    """defines k-ary tree"""
    def __init__(self, val, input_list=[]):
        """defines root node"""
        # if input_list is not list:
        #     return KeyError
        node = Node(val, input_list)
        self.root = node

    def __repr__(self):
        """returns a string of type and address"""
        # return 'node children: {} '.format(lambda x: for x in self.children: return x.val)
        # return '<{} at {}>'.format(type(self, hex(id(self))))

    def __str__(self):
        """string representation of all nodes values"""
        return 'root value: {}'.format(self.root.val)

    def pre_order(self, operation=None):
        """returns node values in a pre-order traversal
           takes an argument operation in the form of a lambda function         
        """

        def _walk(node=None):
            if node is None:
                return

            operation(node)
            
            for child in node.children:
                _walk(child)
        
        if self.root is None:
            return False
        else:
            _walk(self.root)    

    def post_order(self, operation=None):
        """
        returns node values in a pre-order traversal
        takes an argument operation in the form of a lambda function         
        """
        
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)
        
            operation(node)

        if self.root is None:
            return False
        else:
            _walk(self.root)  

    def breadth_first(self, operation=None):
        """
        returns node valuse in beadth first traversal.
        takes an argument operation in the form of a lambda function
        """
        pass