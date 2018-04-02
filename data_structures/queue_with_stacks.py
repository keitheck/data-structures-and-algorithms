from stack.stack import Stack


class Queue_with_stacks:

    def __init__(self, iterable=[]):
        self.stack_back = Stack(iterable)
        self.stack_front = Stack()

    def __topval__(self):
        if self.stack_back.top.val is None:
            print('Queue is empty')
        else:
            print('Next in queue is {}'.format(self.stack_back.top.val))         

    def enqueue(self, val):
        self.stack_back.push(val)
        print('{} added to end of Queue'.format(self.stack_back.top.val))

    def dequeue(self):
        if self.stack_back.top is None:
            raise IndexError("queue is empty")
        x = None
        while self.stack_back.top._next:
            x = self.stack_back.pop()
            self.stack_front.push(x)
            # print('{} added to end of front Queue'.format(self.stack_front.top.val))
        y = self.stack_back.pop()
        while self.stack_front.top:
            x = self.stack_front.pop()
            self.stack_back.push(x)
            # print('{} added to end of back Queue'.format(self.stack_back.top.val))
        print('{} was removed from front of Queue'.format(y))
        return y    
