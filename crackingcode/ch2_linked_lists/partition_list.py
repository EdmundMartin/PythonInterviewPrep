"""
Write code to partition a Linked List so around a value: x

So that all nodes less than x come before all nodes equal or greater than x
"""
from typing import Optional
from crackingcode.ch2_linked_lists.single_linked_list import (
    SinglyLinkedNode,
    linked_list_from_list,
    linked_list_to_python_list,
)


def partition(node: SinglyLinkedNode, target: int) -> SinglyLinkedNode:
    head: Optional[SinglyLinkedNode] = node
    tail: Optional[SinglyLinkedNode] = node

    while node:
        next_node = node.next
        if node.value < target:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next_node
    tail.next = None
    return head


if __name__ == "__main__":
    test_data = linked_list_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    result = partition(test_data, 7)
    assert linked_list_to_python_list(result) == [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11]
