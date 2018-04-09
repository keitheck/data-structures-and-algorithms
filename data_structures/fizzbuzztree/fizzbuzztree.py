def fizzbuzztree(tree):
    """a funtion that takes a tree as an arument and replaces leaf
    values with fizz if divisable by 3, buzz if by 5, and fizzbuzz if 15"""
    node = tree.root
    
    if node is None:
        return 'Tree is empty. Please use a populated tree of integers'

    def _walk(node):
        if node is None:
            return tree

        if node.left is not None:
            _walk(node.left) 

        if node.right is not None:
            _walk(node.right)  

        if node.val % 15 == 0:
            node.val = 'fizzbuzz'

        elif node.val % 5 == 0:
            node.val = 'buzz'

        elif node.val % 3 == 0:
            node.val = 'fizz'

    _walk(tree.root)                    
       
