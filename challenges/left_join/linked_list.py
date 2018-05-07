class Node:

    def __init__(self, val, next=None):
        """
        set up __init__ function that sets the value to next to None (sets as last node)
        """
        self.val = val
        self._next = next  # this will update to the location of the next node when next node created

    def __str__(self):
        """
        this is a special method that we can define to represent an output 
        value for an instantiated object
        """
        return '{val}'.format(val=self.val)


class LinkedList:
    """
    This will create an empty linked list
    """
    def __init__(self, iter=[]):
        self.head = None  # not a data node, points to first element of list
        self._current = None
        self._size = 0

        for item in reversed(iter):
            # want to reverse the list so items are inserted in correct order
            self.insert(item)

    def __repr__(self):
        """
        return custom repr
        """
        if self.head is None:
            return '<head> => None'

        return '<head> => {}'.format(self.head)

    def __len__(self):
        """
        returns the length of the linked list
        """
        return self._size

    def insert_at_last(self, data):
        pass

    def insert(self, val):
        """
        inserts node at the head of list as this is more performant for most 
        purposes.  
        step one: make a node =>  node = Node(val)
        step two: point to the current head  => node.next = self.head
        step three: reassign head   =>  self.head = node

        We made our Node() accept an argument for next node, so:
                => node = Node(val, self.head)
        """
        try:
            if type is str or int:
                self.head = Node(val, self.head)
                # print('inserted self.head=> {}'.format(self.head))
                # print('inserted self.head.val => {}'.format(self.head.val))
                self._size += 1

        except NameError:
            print("""
            Please enter only a string or an integer
            """)

    def find(self, x):
        """
        Define a method called find which takes any value as an 
        argument and returns True or False depending on whether that 
        value exists as a Node value within the list. 
        """
        node_index = self.head
        while node_index is not None:
            if node_index.val == x:
                return True
            node_index = node_index._next
        return False

    def __str__(self):
        """
        doc string
        """
        node = self.head
        data_set = '(HEAD) '
        while(node):
            data_set += '{}: '.format(node.val)
            node = node._next
        data_set += '(NULL)'
        return data_set

    def append(self, val):
        """add node to end of linked list"""
        if self._size == 0:
            self.insert(val)
            return
        node_index = self.head
        if not node_index._next:
            node_index = Node(val)

        while node_index._next:
            node_index = node_index._next
            print('while loop')
            print('node index => {}'.format(node_index))
        node_index._next = Node(val) 
        self._size += 1     
        return 'length => {}'.format(self.__len__())  

    def insertBefore(self, val, newVal):
        """add node with new Val before node with val"""
        if self._size == 0:
            return 'This Linked List is Empty'
        previous_node = self.head
        """check if previous_node matches val"""
        if previous_node.val == val:
            self.head = Node(newVal, previous_node)
            return self
        if previous_node._next:
            x = previous_node._next
            while x:
                if x.val == val:
                    print('x', x)
                    new_insert = Node(newVal, x)
                    previous_node._next = new_insert
                    self._size += 1
                    print('length => {}'.format(self.__len__()))
                    return
                previous_node = x
                x = x._next
        return 'did not insert, key value not found'    

    def insertAfter(self, val, newVal):
        """add node with new val after node with val"""
        if self._size == 0:
            return 'This Linked List is Empty, did not insert new value' 
        node = self.head
        while node:
            # import pdb; pdb.set_trace()
            if node.val == val:
                print('Node.val => {}'.format(node.val))
                newNode = Node(newVal,node._next)
                node._next = newNode
                self._size += 1
                return
            node = node._next    
        return 'did not insert, key value not found'   

    def kthFromEnd(self, k):
        """return node from index k of linked list"""
        # ll_length = self._size
        x = self._size - (k + 1)
        node = self.head
        counter = 0
        while node:
            if counter == x:
                return node
            counter += 1
            node = node._next
        raise IndexError('requested node outside linked list length')

    def hasLoop(self):
        """returns false if no looped node reference"""
        self.node1 = self.head
        if self.node1 is None:
            return False
        else:
            self.node2 = self.node1._next
            while self.node2 is not None:
                if self.node1 is self.node2:
                    return True
                self.node2 = self.node2._next
                if self.node1 is self.node2:
                    return True
                if self.node2 is None:
                    return False
                self.node1 = self.node1._next
                self.node2 = self.node2._next
