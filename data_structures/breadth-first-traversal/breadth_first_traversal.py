from queue import Queue
from bst import BST


def breadthFirstTraversal(tree, prnt=print):
    """
    takes a tree as an argument and returns 
    the node values in breadth first traversal order
    """
    
    if tree.root is None:
        return False

    q = Queue()

    prnt(tree.root.val)
    
    if tree.root.left:
        q.enqueue(tree.root.left)

    if tree.root.right:    
        q.enqueue(tree.root.right)
    
    first = q.front()

    while first:
        node = first.val
        prnt(node.val)
        if node.left:
            q.enqueue(node.left)
        if node.right:    
            q.enqueue(node.right)
        front = first._next    

           
