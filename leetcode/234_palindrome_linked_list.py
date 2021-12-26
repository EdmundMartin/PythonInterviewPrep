from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionNaive:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == self.reverse_list(values[::])

    def reverse_list(self, target_list):
        i = 0
        j = len(target_list) - 1
        while i < j:
            target_list[i], target_list[j] = target_list[j], target_list[i]
            i += 1
            j -= 1
        return target_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first_pos = head
        second_pos = second_half_start

        while result and second_pos is not None:
            if first_pos.val != second_pos.val:
                result = False
            first_pos = first_pos.next
            second_pos = second_pos.next

        return result

    def end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = not current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(2)
    root.next.next.next = ListNode(1)

    assert SolutionNaive().is_palindrome(root) is True

    second_root = ListNode(1)
    second_root.next = ListNode(2)

    assert SolutionNaive().is_palindrome(second_root) is False