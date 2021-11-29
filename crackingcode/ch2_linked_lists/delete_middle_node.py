"""
Implement algo to delete a node in the middle of a singly linked list,
given only access to that node.

Say if you can delete the node or not.
"""
from typing import Optional
from crackingcode.ch2_linked_lists.single_linked_list import SinglyLinkedNode


def delete_node(node: Optional[SinglyLinkedNode]) -> bool:
    if node is None or node.next is None:
        return False
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next
    return True
