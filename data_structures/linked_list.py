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
        if nodes:
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

    def add_first(self, new_node: Node):
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node: Node):
        if self.head is None:
            self.head = new_node
            return
        # this traverses the whole list of elements and sets
        # current_node to the last element
        for current_node in self:
            pass

        current_node.next = new_node

    def add_after(self, target_node_data, new_node: Node):
        if self.head is None:
            raise Exception("Linked list is empty")
        for node in self:
            if node.data == target_node_data:
                nex_item = node.next
                node.next = new_node
                new_node.next = nex_item
                return

        raise Exception(f"Node with data {target_node_data} is not present in list")

    def add_before(self, target_node_data, new_node: Node):
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            # find previous item
            if prev_node.next.data == target_node_data:
                return self.add_after(prev_node.data, new_node)
            prev_node = node.next

        raise Exception(f"Node with data {target_node_data} is not present in list")
