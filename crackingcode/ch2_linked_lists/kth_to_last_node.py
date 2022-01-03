from typing import Optional

from crackingcode.ch2_linked_lists.single_linked_list import (
    SinglyLinkedNode,
    linked_list_from_list,
)


def nth_to_last(head: SinglyLinkedNode, k: int) -> Optional[SinglyLinkedNode]:
    fast = head
    slow = head

    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


if __name__ == "__main__":
    result = linked_list_from_list([1, 2, 3, 4, 6, 7, 8, 9, 10])
    node = nth_to_last(result, 3)
    assert node.value == 8
