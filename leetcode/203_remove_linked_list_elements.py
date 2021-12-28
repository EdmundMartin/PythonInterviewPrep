from typing import Optional
from leetcode.utils import linked_list_from_list, linked_list_to_python_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 68 ms, faster than 70.77% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.2 MB, less than 68.10% of Python3 online submissions for Remove Linked List Elements.
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head
        prev = None
        while current_node:
            if current_node.val == val:
                if prev:
                    prev.next = current_node.next
                    current_node = current_node.next
                else:
                    head = current_node.next
                    current_node = current_node.next
            else:
                prev = current_node
                current_node = current_node.next
        return head


if __name__ == '__main__':
    front = ListNode(7)
    front.next = ListNode(7)
    front.next.next = ListNode(7)
    front.next.next.next = ListNode(7)

    result = Solution().removeElements(front, 7)
    assert result is None

    front = linked_list_from_list([1, 2, 6, 3, 4, 5, 6])
    result = Solution().removeElements(front, 6)
    assert linked_list_to_python_list(result) == [1, 2, 3, 4, 5]