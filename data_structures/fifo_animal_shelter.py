from stack.stack import Stack


class AnimalShelter:

    def __init__(self, iterable=[]):
        self.stack_back = Stack(iterable)
        self.stack_front = Stack()

        # import pdb; pdb.set_trace()

    def __topval__(self):
        if self.stack_back.top.val is None:
            print('Queue is empty')
        else:
            print('Next in queue is {}'.format(self.stack_back.top.val))         

    def enqueue(self, val):
        self.stack_back.push(val)
        print('{} added to end of Queue'.format(self.stack_back.top.val))

    def dequeue(self, pref):
        if self.stack_back.top is None:
            raise IndexError("queue is empty")
        x = None
        while self.stack_back.top._next:
            x = self.stack_back.pop()
            self.stack_front.push(x)
            # print('{} added to end of front Queue'.format(self.stack_front.top.val))
        y = self.stack_back.pop()
        print(y)
        if y != 'cat' or 'dog':
            output = y
            while self.stack_front.top:
                x = self.stack_front.pop()
                self.stack_back.push(x)
                return output

        if str(y) == pref:
            output = y
            while self.stack_front.top:
                x = self.stack_front.pop()
                self.stack_back.push(x)
                return output
        else:
            self.stack_front.push(y)
            while self.stack_front.top:
                x = self.stack_front.pop()
                if x == pref:
                    output = x
                else:    
                    self.stack_back.push(x)

            # print('{} added to end of back Queue'.format(self.stack_back.top.val))
        print('oldest {} was removed from Queue'.format(output))
        return output
