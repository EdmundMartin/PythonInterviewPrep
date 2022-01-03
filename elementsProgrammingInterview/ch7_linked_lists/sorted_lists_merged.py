from typing import Optional

from elementsProgrammingInterview.ch7_linked_lists.linked_list_bootcamp import (
    ListNode,
    linked_list_from_list,
    linked_list_to_python_list,
)


def merge_two_sorted_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_head = tail = ListNode()

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    tail.next = l1 or l2

    return dummy_head.next


if __name__ == "__main__":
    list_one = linked_list_from_list([1, 10, 20, 30, 40, 45, 50, 55, 60])
    list_two = linked_list_from_list([1, 8, 18, 33, 43, 52, 58, 63])

    result = merge_two_sorted_lists(list_one, list_two)
    assert linked_list_to_python_list(result) == [
        1,
        1,
        8,
        10,
        18,
        20,
        30,
        33,
        40,
        43,
        45,
        50,
        52,
        55,
        58,
        60,
        63,
    ]
