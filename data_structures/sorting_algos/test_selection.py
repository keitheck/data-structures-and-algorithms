from selection import selection_sort
import pytest

def test_empty():
    """
    Tests empty and length 1 Lists return correctly.
    """
    assert selection_sort([]) == []
    assert selection_sort([8]) == [8]


def test_TypeError():
    """
    Tests non-list types throw TypeError.
    """
    with pytest.raises(TypeError):
        assert selection_sort('string') 


def test_one():
    """
    Tests returns as expected.
    """
    assert selection_sort([7, 2, 6, 3, 4, 1, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_two():
    """
    Tests returns as expected.
    """
    assert selection_sort([7, -3, 6, -99, 4, 1, 12, 8, 401, 5]) == [-99, -3, 1, 4, 5, 6, 7, 8, 12, 401]    