from leetcode.utils import linked_list_to_python_list, linked_list_from_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = {}
        first = head
        while first:
            if first.val in counter:
                counter[first.val] += 1
            else:
                counter[first.val] = 1
            first = first.next

        second = final_head = head
        prev = None
        while second:
            if counter[second.val] > 1:
                if prev is None:
                    tmp = second.next
                    final_head = tmp
                    second = tmp
                else:
                    tmp = second.next
                    prev.next = tmp
                    second = tmp
            else:
                prev = second
                second = second.next
        return final_head


if __name__ == "__main__":
    test_input = linked_list_from_list([1, 2, 3, 2])
    result = Solution().deleteDuplicatesUnsorted(test_input)
    assert linked_list_to_python_list(result) == [1, 3]

    test_input = linked_list_from_list([2, 1, 1, 2])
    result = Solution().deleteDuplicatesUnsorted(test_input)
    assert linked_list_to_python_list(result) == []

    test_input = linked_list_from_list([3, 2, 2, 1, 3, 2, 4])
    result = Solution().deleteDuplicatesUnsorted(test_input)
    assert linked_list_to_python_list(result) == [1, 4]
