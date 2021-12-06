from typing import Optional

from crackingcode.ch2_linked_lists import SinglyLinkedNode


def find_beginning(head: SinglyLinkedNode) -> Optional[SinglyLinkedNode]:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        # No loop return
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast
