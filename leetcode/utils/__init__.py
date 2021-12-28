from typing import List, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_from_list(values):
    dummy_head = ListNode(0)
    root = dummy_head
    for val in values:
        root.next = ListNode(val)
        root = root.next
    return dummy_head.next


def linked_list_to_python_list(head) -> List[Any]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values