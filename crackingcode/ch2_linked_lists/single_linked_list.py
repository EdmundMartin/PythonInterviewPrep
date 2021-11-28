from typing import Optional, List, Any


class SinglyLinkedNode:

    def __init__(self, value: int):
        self.value = value
        self.next: Optional[SinglyLinkedNode] = None

    def __str__(self):
        return f"<LinkedListNode, value: {self.value}>"


def linked_list_to_python_list(head) -> List[Any]:
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


def linked_list_from_list(values: List[Any]):
    dummy_head = SinglyLinkedNode(0)
    root = dummy_head
    for val in values:
        root.next = SinglyLinkedNode(val)
        root = root.next
    return dummy_head.next
