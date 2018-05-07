from hash_table import HashTable
import pytest 

@pytest.fixture
def empty_hash():
    """
    Returns empty hash table.
    """
    hash_table = HashTable()
    return hash_table


@pytest.fixture
def insert_hash():
    """
    Returns hash table with single node added to several indexes.
    """
    ht = HashTable()
    ht.set('a', 'aa')
    ht.set('CodeFellows', 'school')
    return ht


@pytest.fixture
def insert_hash2():
    """
    Returns hash table with single node added to several indexes.
    """
    ht = HashTable()
    ht.set('b', 'bb')
    ht.set('CodeFellows', 'school')
    ht.set('tree', 'shrub')
    return ht    
