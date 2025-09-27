from .Node import *

class BinarySearchTree(object):
    def __init__(self, head=None):
        self._head = head #
        self._n = 0 if head is None else 1

    def getHead(self):
        return self._head

    def getNElements(self):
        return self._n

    def search(self, value, parent=None, depth=0):
        if self._n == 0:
            return None

        if depth == 0:
            parent = self._head

        if parent == None:
            return None

        if parent.getValue() == value:
            return parent
        elif parent.getValue() < value:
            return self.search(value, parent.getRightChild(), depth+1)
            #depth -= 1
        else:
            return self.search(value, parent.getLeftChild(), depth+1)
            #depth -= 1



    def insert(self, value, parent=None, depth=0):
        if self._n == 0:
            self._n += 1
            self._head = Node(value)
            return

        if depth == 0:
            parent = self._head

        if value >= parent.getValue(): # go throught right branch

            if not parent.getRightChild():
                parent.setRightChild(value)
                self._n += 1
                return
            else:
                self.insert(value, parent.getRightChild(), depth+1)
                depth -= 1

        else: # go throught left branch
            if not parent.getLeftChild():
                parent.setLeftChild(value)
                self._n += 1
                return
            else:
                self.insert(value, parent.getLeftChild(), depth+1)
                depth -= 1

    def delete(self, value, depth=0):
        """
            RULES

            - If the node to be canceled hasn't children, simply drop it
            - If the node to be canceled has only one child, drop it
                and replace the child with the parent
            - If the node to be canceled has both children, then
                - move to the right branch and then traverse all the left
                  branches until the last possible one
                - if the successor has a right child (it's not possible to own
                  a left one due to the previous bullet), put the right child
                  where previously the parent was located
        """

        if self._n == 0:
            return None


        curr_node = self._head
        parent = None

        node_to_delete = None
        while curr_node is not None:
            if value > curr_node.getValue():
                parent = curr_node
                curr_node = curr_node.getRightChild()
            elif value < curr_node.getValue():
                parent = curr_node
                curr_node = curr_node.getLeftChild()
            else:
                node_to_delete = curr_node
                break

        if node_to_delete is None:
            return None

        has_left = node_to_delete.getLeftChild() is not None
        has_right = node_to_delete.getRightChild() is not None

        def _replace_in_parent(parent_node, old_child, new_child):
            if parent_node is None:
                self._head = new_child
                return
            if parent_node.getLeftChild() is old_child:
                parent_node.setLeftChild(new_child)
            elif parent_node.getRightChild() is old_child:
                parent_node.setRightChild(new_child)

        if not has_left and not has_right:
            _replace_in_parent(parent, node_to_delete, None)
            self._n -= 1
            return True

        if has_left and not has_right:
            _replace_in_parent(parent, node_to_delete, node_to_delete.getLeftChild())
            self._n -= 1
            return True

        if not has_left and has_right:
            _replace_in_parent(parent, node_to_delete, node_to_delete.getRightChild())
            self._n -= 1
            return True

        parent_leaf = node_to_delete
        leaf = node_to_delete.getRightChild()
        while leaf.getLeftChild() is not None:
            parent_leaf = leaf
            leaf = leaf.getLeftChild()

        node_to_delete.setValue(leaf.getValue())

        if parent_leaf is node_to_delete:
            parent_leaf.setRightChild(leaf.getRightChild())
        else:
            parent_leaf.setLeftChild(leaf.getRightChild())

        self._n -= 1
        return True


    def show(self):
        pass