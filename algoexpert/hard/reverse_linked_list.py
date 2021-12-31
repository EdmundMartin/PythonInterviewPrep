from typing import Any


class LinkedList:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


def reverse_linked_list(head: LinkedList):
    current_node = head
    tail = None
    while current_node:
        next_node = current_node.next
        current_node.next = tail
        tail = current_node
        current_node = next_node
    return tail
