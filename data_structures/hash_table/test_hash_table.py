from hash_table import HashTable
import pytest


def test_TypeError_hash_key(empty_HT):
    """tests that TypeError is raised when non-string key used"""
    with pytest.raises(TypeError):
        empty_HT.hash_key(1)
    with pytest.raises(TypeError):
        empty_HT.hash_key([1, 2, 3])
    with pytest.raises(TypeError):
        empty_HT.hash_key({'test': 8})


def test_hash_key(empty_HT):
    """test hash_key returns expexted int value"""
    ht = empty_HT
    assert ht.hash_key('a') == 97
    assert ht.hash_key('CodeFellows') == 87
    assert ht.hash_key('the rain in spain falls mainly in the plain') == 933

