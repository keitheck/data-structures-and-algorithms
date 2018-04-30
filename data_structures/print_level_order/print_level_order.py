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
        """walks nodes in a pre-order traversal
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
        walks nodes in a pre-order traversal
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
        walks nodes in beadth first traversal.
        takes an argument operation in the form of a lambda function
        """
        def _walk(iterable):
            node_list = []
            for item in iterable:
                operation(item)
                for child in item.children:
                    node_list.append(child)

            if len(node_list):
                _walk(node_list)

        if self.root:
            _walk([self.root])

    def insert(self, val, searchval):
        """
        method that adds a node with val as value as a child of node with nodeval as value
        """     
        node = Node(val, [])   
        self.breadth_first(lambda x: x.children.append(node) if x.val == searchval else False)


def print_level_order(tree):
    '''takes a ktree and prints each level on a single line'''
    
    if not isinstance(tree, Ktree):
        raise TypeError('argument must be of type <KTree>')

    final_output = []

    def _walk(current):
        output_list = []
        node_list = []
        for node in current:
            output_list.append(str(node.val))
            
            for child in node.children:
                node_list.append(child)

        # print('print_output_fired')
        print_output = ' '.join(output_list)
        final_output.append(print_output)

        if len(node_list):
            _walk(node_list)

    if tree.root:
        _walk([tree.root]) 

    # print(final_output) # this line will print the list
    print('\n'.join(final_output))  # this line will print the list with each level on its own line
    return final_output  # adding a return of final_output list for testing