from typing import Optional

from crackingcode.ch2_linked_lists import SinglyLinkedNode


class TailResult:

    def __init__(self, tail: Optional[SinglyLinkedNode], size: int):
        self.tail = tail
        self.size = size


def find_intersection(first: SinglyLinkedNode, second: SinglyLinkedNode) -> Optional[SinglyLinkedNode]:
    if first is None or second is None:
        return None

    first_result = get_tail_and_size(first)
    second_result = get_tail_and_size(second)

    if first_result.tail != second_result.tail:
        return None

    if first_result.size < second_result.size:
        shorter, longer = first, second
    else:
        longer, shorter = first, second

    longer = get_kth_node(longer, abs(first_result.size - second_result.size))

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return longer


def get_tail_and_size(node: SinglyLinkedNode) -> TailResult:
    if not node:
        return TailResult(None, 0)
    size = 1
    current = node
    while current.next:
        size += 1
        current = current.next
    return TailResult(current, size)


def get_kth_node(node: SinglyLinkedNode, k: int) -> SinglyLinkedNode:
    current = node
    while k > 0 and current:
        current = current.next
        k -= 1
    return current
