from queue import Queue
from bst import BST


def breadthFirstTraversal(tree):
    """
    takes a tree as an argument and returns 
    the node values in breadth first traversal order
    """
    l = []
    
    if tree.root is None:
        return l

    q = Queue()
    l.append(tree.root.val)
    print(l)
    
    if tree.root.left:
        q.enqueue(tree.root.left)

    if tree.root.right:    
        q.enqueue(tree.root.right)
    
    first = q.dequeue()
    while first.val:
        node = first.val
        l.append(node.val)
        print(l)

        if node.left:
            q.enqueue(node.left)
        if node.right:    
            q.enqueue(node.right)

        if q.back is not None:
            first = q.dequeue()
        else:        
            return l

           
