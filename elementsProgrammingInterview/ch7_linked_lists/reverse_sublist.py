from typing import Optional

from elementsProgrammingInterview.ch7_linked_lists.linked_list_bootcamp import ListNode


def reverse_sublist(l: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, l)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            temp,
        )

    return dummy_head.next
