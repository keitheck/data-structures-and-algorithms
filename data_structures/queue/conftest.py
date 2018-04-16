from queue import Queue
import pytest

@pytest.fixture
def empty_queue():
    """returns and empty queue"""
    return Queue()


@pytest.fixture
def small_queue():
    """returns filled queue"""
    return Queue([1,2,3,4,5])