from typing import Optional
from leetcode.utils import linked_list_from_list, linked_list_to_python_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    head = linked_list_from_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 2)
    print(linked_list_to_python_list(result))

    head = Solution().removeNthFromEnd(linked_list_from_list([1]), 1)
    print(head)

    head = Solution().removeNthFromEnd(linked_list_from_list([1, 2]), 1)
    print(linked_list_to_python_list(head))
