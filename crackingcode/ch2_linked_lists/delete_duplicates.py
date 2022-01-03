from typing import Optional

from crackingcode.ch2_linked_lists.single_linked_list import (
    SinglyLinkedNode,
    linked_list_to_python_list,
    linked_list_from_list,
)


def delete_duplicates(node: SinglyLinkedNode) -> SinglyLinkedNode:
    head = node
    seen_values = set()
    previous: Optional[SinglyLinkedNode] = None
    while node:
        if node.value in seen_values:
            previous.next = node.next
        else:
            seen_values.add(node.value)
            previous = node
        node = node.next
    return head


def delete_duplicates_no_buffer(node: SinglyLinkedNode) -> SinglyLinkedNode:
    head = node
    current = node
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head


if __name__ == "__main__":
    test_list = linked_list_from_list([1, 1, 1, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8])
    result = delete_duplicates(test_list)
    assert linked_list_to_python_list(result) == [1, 3, 4, 5, 6, 7, 8]

    test_list = linked_list_from_list([1, 1, 1, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8])
    result = delete_duplicates_no_buffer(test_list)
    assert linked_list_to_python_list(result) == [1, 3, 4, 5, 6, 7, 8]
