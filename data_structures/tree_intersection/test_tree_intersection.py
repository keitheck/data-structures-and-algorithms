from tree_intersection import tree_intersection as tr 
import pytest


def test_matches_one(short_depth, medium_depth):
    """
    test if algorithm returns as expected
    """
    assert tr(short_depth, medium_depth) == [10, 5, 16]


def test_matches_two(medium_depth, short_depth):
    """
    tests that changing order of input yields same answer
    """
    assert tr(medium_depth, short_depth) == [10, 5, 16]


def test_matches_three(long_depth, medium_depth):
    """
    test if algorithm returns as expected
    """
    assert tr(long_depth, medium_depth) == [10, 5, 2, 4, 7, 6, 8, 16, 12, 13, 17]


