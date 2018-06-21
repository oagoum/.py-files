class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

class LinkedList:
    def __init__(self):
        self._start = None

    def insert(self, data):
        if self._start is None:
            node = Node(data)
            self._start = node
        else:
            node = Node(data)
            node._next = self._start
            self._start = node

    def remove(self):
        if self._start is None:
            return None
        else:
            r = self._start
            self._start = self._start._next

            return r._data

    def printOut(self):
        go = self._start
        while go is not None:
            print(go._data)
            go = go._next


"""
l = LinkedList()
l.insert(3)
l.insert(2)
l.insert(1)
l.remove()
l.printOut()
"""

