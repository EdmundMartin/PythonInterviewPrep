from typing import Any, List, Optional


class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional["LinkedList"] = None


def linked_list_to_python_list(head) -> List[Any]:
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


def linked_list_from_list(values: List[Any]):
    dummy_head = LinkedList(0)
    root = dummy_head
    for val in values:
        root.next = LinkedList(val)
        root = root.next
    return dummy_head.next


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 4, 5, 5, 6, 6, 8, 9]
    result = linked_list_from_list(test_array)
    print(linked_list_to_python_list(result))
