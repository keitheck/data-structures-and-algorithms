from node import Node


class Queue:

    def __init__(self, iterable=[]):
        """runs on initiation of class Queue"""
        self.back = None
        self._size = 0
        
        for item in iterable:
            print(item)
            self.enqueue(item)
            
    def __len__(self):
        """magic method that returns length of the queue"""
        return self._size

    def __repr__(self):
        """technical representation"""
        current = self.back
        while current._next:
            current = current._next
        print("node at front of queue => {}".format(current.val))

    def __str__(self):
        """return the value of back of the queue"""
        try:
            print("Back of Queue => {}".format(self.back))
        except ValueError:
            print('Queue is empty')
    
    def enqueue(self, val):
        """add a value to the back of the queue with an O(1) time"""
        print('fired')

        if self.back:
            self.back = Node(val, self.back)

        else:
            # print('else: self.back = Node(val)')
            self.back = Node(val)

        self._size += 1
        # print('self.back = self.back._next.Node(val)')

    def dequeue(self):
        """removes and returns node value from front of queue"""
        
        if self.back is None:
            raise ValueError('No value to rueturn, Queue is empty')

        if self.back._next is None:
            x = self.back
            self.back = None
            self._size = 0
            return x.val    

        dequeue = self.back

        while dequeue._next:
            prev = dequeue
            dequeue = dequeue._next
            
        prev._next = None
        self._size -= 1
        return dequeue


