from bst import BST


def tree_intersection(tree1, tree2):
    """
    This is a function that takes two trees and returns a list of common
    values.
    """
    
    tree_list1 = []
    tree_list2 = []
    output_list = []

    tree1.pre_order_traversal(lambda x: tree_list1.append(x.val))
    tree2.pre_order_traversal(lambda y: tree_list2.append(y.val))

    for item in tree_list2:
        if item in tree_list1:
            if item not in output_list:
                output_list = output_list + [item]

    return output_list
