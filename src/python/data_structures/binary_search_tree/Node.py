
class Node(object):
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left_child = left
        self._right_child = right

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def getLeftChild(self):
        return self._left_child

    def getRightChild(self):
        return self._right_child

    def setLeftChild(self, value):
        self._left_child = Node(value)

    def setRightChild(self, value):
        self._right_child = Node(value)