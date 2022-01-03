# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        current_node = head
        prev: Optional[ListNode] = None
        while current_node:
            if prev and prev.val == current_node.val:
                while current_node and current_node.val == prev.val:
                    prev.next = current_node.next
                    current_node = current_node.next
            else:
                prev = current_node
                current_node = current_node.next
        return head


def linked_list_as_list(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    first = ListNode(1)
    first.next = ListNode(1)
    first.next.next = ListNode(2)

    result = Solution().deleteDuplicates(first)
    assert linked_list_as_list(result) == [1, 2]
    # [1,1,2,3,3]
    second = ListNode(1)
    second.next = ListNode(1)
    second.next.next = ListNode(2)
    second.next.next.next = ListNode(3)
    second.next.next.next.next = ListNode(3)

    result = Solution().deleteDuplicates(second)
    assert linked_list_as_list(result) == [1, 2, 3]
