from queue import Queue
from bst import BST


def find_maximum_value(tree):
    """
    takes a tree as an argument and returns
    largest node value
    """
    
    if tree.root is None:
        return False

    l = []
    q = Queue()

    def walk(node):
        if node is None:
            return

        if node.left is not None:
            walk(node.left)
        
        l.append(node.val)

        if node.right is not None:
            walk(node.right)

    walk(tree.root)

    return max(l)










    # l.append(tree.root.val)
    # print(l)
    
    # if tree.root.left:
    #     q.enqueue(tree.root.left)

    # if tree.root.right:    
    #     q.enqueue(tree.root.right)
    
    # first = q.dequeue()
    # while first.val:
    #     node = first.val
    #     l.append(node.val)
    #     print(l)

    #     if node.left:
    #         q.enqueue(node.left)
    #     if node.right:    
    #         q.enqueue(node.right)

    #     if q.back is not None:
    #         first = q.dequeue()
    #     else:        
    #         return l

           
