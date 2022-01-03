from typing import Optional, List, Any


class ListNode:
    def __init__(self, data: int = 0, next: Optional["ListNode"] = None):
        self.next = next
        self.data = data


def search_in_list(l: ListNode, key: int) -> ListNode:
    while l and l.data != key:
        l = l.next
    return l


def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node


def delete_after(node: ListNode) -> None:
    node.next = node.next.next


def linked_list_to_python_list(head) -> List[Any]:
    values = []
    while head:
        values.append(head.data)
        head = head.next
    return values


def linked_list_from_list(values: List[Any]):
    dummy_head = ListNode(0)
    root = dummy_head
    for val in values:
        root.next = ListNode(val)
        root = root.next
    return dummy_head.next
