from linked_list import LinkedList


class HashTable:
    def __init__(self, max_size=1024):
        """
        This initiatates the hash table with empty linked lists in each bucket.
        """

        if type(max_size) is not int:
            raise TypeError

        # linked_list = LinkedList()
        self.max_size = max_size
        # self.buckets = [linked_list] * self.max_size  # this returns the same list in each
        self.buckets = [LinkedList() for _ in range(self.max_size)]

    def hash_key(self, key):
        """
        assigns a int value to key
        """
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """
        inserts {key: val} into hash table.
        """

        if type(key) is not str:
            raise TypeError

        return self.buckets[self.hash_key(key)].insert({key: val})    

        # hash the key; get a location for the bucket to insert into
        # set val into bucket

    def get(self, key):
        """
        uses key to return value from index.
        """

        if type(key) is not str:
            raise TypeError

        node = self.buckets[self.hash_key(key)].head

        while node:
            if key in node.val.keys():
                return node.val[key]
            node = node._next    
        
        return 'key does not exist in hash table'

    def remove(self, key):
        """
        Uses key to remove value from table.
        """
        if type(key) is not str:
            raise TypeError

        temp = self.buckets[self.hash_key(key)]  # this goes to the index assigned from key
        node = temp.head  # this selects the head node of the linked list
        previous = node

        while node:

            if key in node.val.keys():
                if previous is not node:
                    previous._next = node._next
                else:
                    temp.head = node._next
                return node.val[key]
            previous = node
            node = node._next

        return 'key does not exist in hash table'
