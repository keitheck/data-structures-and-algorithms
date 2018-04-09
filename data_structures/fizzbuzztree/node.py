class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'leaf val: {} =>'.format(self.val)

    def __str__(self):
        return 'val => {}'.format(self.val)

