from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        first_pointer = headA
        second_pointer = headB

        while first_pointer != second_pointer:
            first_pointer = headB if first_pointer is None else first_pointer.next
            second_pointer = headA if second_pointer is None else second_pointer.next

        return first_pointer
