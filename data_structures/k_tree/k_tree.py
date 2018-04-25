class Node:
    """defines each node used to build the k-ary tree"""
    def __init__(self, val, children=None):
        self.val = val
        if children is None:
            self.children = []
        self.children = children

    def __repr__(self):
        # return 'node children: {} '.format(lambda x: for x in self.children: return x.val)
        return self.root.val 

    def __str__(self):
        return 'node value: {}'.format(self.val)


class Ktree:
    """defines k-ary tree"""
    def __init__(self, val, children=[]):
        """defines root node"""
        node = Node(val, children)
        self.root = node

    def __repr__(self):
        """returns a string of type and address"""
        # return 'node children: {} '.format(lambda x: for x in self.children: return x.val)
        return '<{} at {}>'.format(type(self, hex(id(self))))

    def __str__(self):
        """string representation of all nodes values"""
        return 'root value: {}'.format(self.root.val)

    def pre_order(self, operation=None):
        """performs operation in pre-order traversal"""
        po_list = []

        def _walk(node=None):
            if node is None:
                return
            print('operation')

            import pdb ; pdb.set_trace()
            po_list.append(node.val)

            for child in node.children:
                _walk(child)
        
        if self.root is None:
            return False
        else:
            _walk(self.root)    





    
    
    # def insert(self, parent_val, val=None):
    #     """function that inserts node into tree"""
    #     node = Node(val)
    #     current = self.root

    #     if self.root.val is None:
    #         self.root = node
    #         return self.root.val

    #     else:
    #         def _search(self, parent_val, node):
    #             if parent_val == current.val:
    #                 current.children.append(node)
    #                 return '{} added to {}'.format(node, parent_val)
    #             for item in node.children:
    #                 _search(item, parent_val, node)    

    # def pre_order(self, operation=None):
    #     def _walk(node=None):
    #         if not Node:
    #             return
    #         operaton(node.val)
    #         for item in node.children:
    #             _walk(item) 
    #     _walk(self.root)           

    # def post_order(self, operation=None):
    #     """function that searches ktree"""
    #     def _walk(node=None):
    #         if not Node:
    #             return
    #         for item in node.children:
    #             _walk(item) 
    #         operaton(node.val)
    #     _walk(self.root)

    # def breadth_first(self):
    #     pass

                