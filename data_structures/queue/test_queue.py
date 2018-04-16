def test_load(empty_queue):
    """tests creation of an empty queue"""
    assert len(empty_queue) == 0


def test_iterable_init(small_queue):
    """test insertion of iterable""" 
    assert len(small_queue) == 5


def test_dequeue(small_queue):
    """test insertion into queue"""  
    assert small_queue.dequeue() == 1    


def test_enqueue(small_queue):
    """test insertion onto back of queue"""
    small_queue.enqueue(6)
    assert len(small_queue) == 6