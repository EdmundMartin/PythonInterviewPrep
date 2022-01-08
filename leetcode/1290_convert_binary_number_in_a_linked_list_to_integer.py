

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return int(''.join([str(num) for num in nums]), 2)