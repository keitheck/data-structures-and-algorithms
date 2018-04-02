from node import Node


class Queue:

    def __init__(self, iterable=[]):
        """runs on initiation of class Queue"""
        self.back = None
        self.front = None
        self._size = 0
        
        for item in iterable:
            print(item)
            self.enqueue(item)
        # try:
        # except TypeError:
        #     print('Pleae instansiate with an iterable')
            
    def __len__(self):
        """magic method that returns length of the queue"""
        return self._size

    def __str__(self):
        """return the value of front of the queue"""
        try:
            q_front = self.front.val
            print("Front")
        except ValueError:
            print('Queue is empty')
    
    def enqueue(self, val):
        """add a value to the back of the queue with an O(1) time"""
        print('fired')
        # node = Node(val)

        if self.back:
            self.back._next = Node(val)
            self.back = self.back._next

        else:
            print('Changed:')
            self.back = Node(val)
            print('self.back = Node(val)')
            self.front = self.back
            print('self.front = self.back')

        self._size += 1
        print('self.back = self.back._next.Node(val)')

    def dequeue(self):
        """removes and returns node value from front of queue"""
        dequeue = None
        if self.front is None:
            raise ValueError('No value to rueturn, Queue is empty')
        else:
            print('dequeval fired')
            dequeval = self.front
            self.front = self.back
            self.back = self.back._next
            self._size = 0
            return dequeval.val


