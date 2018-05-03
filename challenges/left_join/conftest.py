from hash_table import HashTable
import pytest 

@pytest.fixture
def empty_HT():
    """
    Returns empty hash table.
    """
    hash_table = HashTable()
    return hash_table


@pytest.fixture
def insert_HT():
    """
    Returns hash table with single node added to several indexes.
    """
    ht = HashTable()
    ht.set('a', 100)
    ht.set('CodeFellows', 99)
    return ht
