"""
Is Palindrome
Implement a function to check if a linked list is a palindrome.
"""
from crackingcode.ch2_linked_lists import SinglyLinkedNode, linked_list_from_list


# Solution 1 - Reverse and Clone
def is_palindrome(node: SinglyLinkedNode) -> bool:
    reversed_list: SinglyLinkedNode = reverse_and_clone(node)
    return are_equal(node, reversed_list)


def reverse_and_clone(node: SinglyLinkedNode) -> SinglyLinkedNode:
    head = None
    while node:
        n = SinglyLinkedNode(node.value)
        n.next = head
        head = n
        node = node.next
    return head


def are_equal(first: SinglyLinkedNode, second: SinglyLinkedNode) -> bool:
    while first and second:
        if first.value != second.value:
            return False
        first = first.next
        second = second.next
    return first is None and second is None


if __name__ == "__main__":
    palindrome = linked_list_from_list([3, 7, 3])
    not_palindrome = linked_list_from_list([3, 7, 3, 8])
    assert is_palindrome(palindrome) is True
    assert is_palindrome(not_palindrome) is False
