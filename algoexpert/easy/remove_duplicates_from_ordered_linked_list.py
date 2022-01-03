from typing import Optional
from algoexpert.utils.linked_list import (
    linked_list_to_python_list,
    linked_list_from_list,
    LinkedList,
)


def remove_duplicates_from_linked_list(head: LinkedList) -> LinkedList:
    prev: Optional[LinkedList] = None
    current_node = head
    while current_node:
        if prev and prev.value != current_node.value:
            prev.next = current_node
            prev = current_node
        if prev and current_node.next is None:
            if current_node.value == prev.value:
                prev.next = None
        if not prev:
            prev = current_node
        current_node = current_node.next
    return head


def remove_duplicates_from_linked_list_alternate(head: LinkedList) -> LinkedList:
    current_node = head
    while current_node:
        next_node = current_node.next
        while next_node is not None and next_node.value == current_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = next_node
    return head


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 4, 5, 5, 6, 6, 8, 9]
    expected_array = [1, 2, 3, 4, 5, 6, 8, 9]
    linked_list = linked_list_from_list(test_array)
    result = remove_duplicates_from_linked_list(linked_list)
    assert expected_array == linked_list_to_python_list(result)

    linked_list = linked_list_from_list(test_array)
    result = remove_duplicates_from_linked_list_alternate(linked_list)
    assert expected_array == linked_list_to_python_list(result)
