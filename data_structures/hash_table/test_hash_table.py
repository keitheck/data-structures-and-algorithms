from hash_table import HashTable
import pytest


def test_TypeError_hash_key(empty_HT):
    """tests that TypeError is raised when non-string key used."""
    with pytest.raises(TypeError):
        empty_HT.hash_key(1)
    with pytest.raises(TypeError):
        empty_HT.hash_key([1, 2, 3])
    with pytest.raises(TypeError):
        empty_HT.hash_key({'test': 8})


def test_hash_key(empty_HT):
    """test hash_key returns expexted int value."""
    ht = empty_HT
    assert ht.hash_key('a') == 97
    assert ht.hash_key('CodeFellows') == 87
    assert ht.hash_key('the rain in spain falls mainly in the plain') == 933


def test_set_raises_typerror(insert_HT):
    """test catches typerror."""
    ht = insert_HT
    with pytest.raises(TypeError):
        ht.set(1, 1)
    with pytest.raises(TypeError):
        ht.set([1, 2, 3], 1)
    with pytest.raises(TypeError):
        ht.set({'test': 8}, 1)


def test_set(insert_HT):
    """tests set works as expected."""
    ht = insert_HT
    ht.set('b', 999)
    assert ht.buckets[98].head.val['b'] == 999


def test_set_2(insert_HT):
    """tests set works as expected on multiple insert of same hash key val."""
    ht = insert_HT
    ht.set('PP', 6)
    ht.set('xx', 999)
    assert ht.buckets[240].head._next.val['PP'] == 6    


def test_get_raises_typerror(insert_HT):
    """test catches typerror."""
    ht = insert_HT
    with pytest.raises(TypeError):
        ht.get(1)
    with pytest.raises(TypeError):
        ht.get([1, 2, 3])
    with pytest.raises(TypeError):
        ht.get({'test': 8})


def test_get(insert_HT):
    """
    tests get method returns as expected.
    """
    assert insert_HT.get('a') == 100
    assert insert_HT.get('CodeFellows') == 99
    assert insert_HT.get('codefellows') == 'key does not exist in hash table'


def test_remove(insert_HT):
    """
    tests removal returns as expected.
    """    
    assert insert_HT.remove('a') == 100
    ht = insert_HT
    ht.set('PP', 6)
    ht.set('xx', 999)
    assert ht.remove('xx') == 999
    assert ht.remove('PP') == 6


def test_remove_2(insert_HT):
    """
    Tests removal of key not in hash table returns correctly
    """
    assert insert_HT.remove('Dog') == 'key does not exist in hash table'


def test_remove_raises_typerror(insert_HT):
    """test catches typerror"""
    ht = insert_HT
    with pytest.raises(TypeError):
        ht.remove(1)
    with pytest.raises(TypeError):
        ht.remove([1, 2, 3])
    with pytest.raises(TypeError):
        ht.remove({'test': 8})


def test_max():
    """
    Tests max size must be type int
    """
    with pytest.raises(TypeError):
        HashTable('muffin')