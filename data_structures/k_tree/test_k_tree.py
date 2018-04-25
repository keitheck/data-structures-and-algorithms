from .k_tree import Ktree
import pytest


def test_empty_tree(height_one_tree):
    """test root val of single node tree"""
    assert height_one_tree.root.val is 0


def test_val_root_filled_tree(depth_one_tree):
    """test root of filled tree"""
    assert depth_one_tree.root.val is 0  

def test_children_tree(depth_one_tree):
    """test root of filled tree"""
    assert depth_one_tree.root.children == [1, 2, 3, 4]    


# def test_insert_empty_tree_correct_val(empty_tree):
#     empty_tree.insert(1) 
#     assert empty_tree.root.val is 1