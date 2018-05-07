from mergesort import mergesort
import pytest


def test_one():
    """
    Tests returns short list sorted correctly.
    """
    assert mergesort([1, 4, 3, 8, 5, 9, 7, 6]) == [1, 3, 4, 5, 6, 7, 8, 9]


def test_typeerror():
    """
    Tests TypeError caught if wrong data type used as argument
    """
    with pytest.raises(TypeError):
        assert mergesort('string')


def test_empty_list():
    """
    Tests empty list and list legth one returned
    """
    assert mergesort([]) == []
    assert mergesort([99]) == [99]


def test_large_list():
    """
    Tests long list sorted correctly.
    """
    assert mergesort([3000, 5, 2234, 56007, 23232, 45, 6, 9, 22, 4567, 896, 4009888, 321, 345, 677, 897, 590, 774, 1243, 1, 642]) == [1, 5, 6, 22, 45, 321, 590, 642, 677, 774, 897, 3000, 4567, 23232, 56007, 4009888]