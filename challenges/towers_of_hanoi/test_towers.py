import pytest
from towers_of_hanoi import recursive_function, tower


def test_recursive():
    """test if recursive function works with positive int"""
    x = []
    assert recursive_function(10) == [10,9,8,7,6,5,4,3,2,1]


def test_recursive2():
    """test if recursive function works with zero int"""
    x = []
    assert recursive_function(0) == []


def test_recursive3():
    """test if recursive function works with negative int"""
    x = []
    assert recursive_function(-10) == []     


def test_tower():
    """test tower 2 disks"""
    assert tower(2, "a", "b", "c") == ["(1, 'from', 'a', 'to', 'c')", "(2, 'from', 'a', 'to', 'b')", "(1, 'from', 'c', 'to', 'b')"]  
        

def test_tower2():
    """test tower 0 disks"""
    assert tower(0, "a", "b", "c") == "empty, not moves possible"


def test_tower3():
    """test tower 1 disks"""
    assert tower(1, "a", "b", "c") == ["(1, 'from', 'a', 'to', 'c')", "(2, 'from', 'a', 'to', 'b')", "(1, 'from', 'c', 'to', 'b')", "(1, 'from', 'a', 'to', 'b')"]

