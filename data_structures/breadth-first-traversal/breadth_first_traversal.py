from queue import Queue
from bst import BST


def breadthFirstTraversal(tree):
    """
    takes a tree as an argument and returns 
    the node values in breadth first traversal order
    """
    
    q = Queue()

    node = tree.root
    q.enqueue(node.left)
    q.enqueue(node.right)
    print(node.val)
    while q:
        node = q.dequeue()
        print(node.val)
        if node.left:
            q.enqueue(node.left)
        if node.right:    
            q.enqueue(node.right)

    return        
