"""
Reminder: https://realpython.com/linked-lists-python/
Summary - linked lists have better performance for inserting at a non-last position since
you don't have to shift the entire sequence unlike in a regular list.
"""
from typing import Optional, List


class Node:
    def __init__(self, data):  # noqa
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes=Optional[List[Node]]):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        obj_repr = str(node.data)
        while node.next:
            node = node.next
            obj_repr += " -> " + str(node.data)
        return obj_repr

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_first(self, node: Node):
        pass

    def add_last(self, node: Node):
        pass

    def add_after(self, target_node_data, node: Node):
        pass
