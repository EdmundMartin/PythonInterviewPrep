from typing import Optional, List
from leetcode.utils import linked_list_from_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        values = []
        current_node = head
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next

        results = [0] * len(values)

        stack = []
        for idx in range(len(values)):

            while len(stack) > 0 and values[stack[-1]] < values[idx]:
                top = stack.pop()
                results[top] = values[idx]

            stack.append(idx)
        return results


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]):

        current_node = head
        stack = []
        results = []
        idx = 0
        while current_node:

            while len(stack) > 0:
                node_idx, node = stack[-1]
                if node.val < current_node.val:
                    results[node_idx] = current_node.val
                    stack.pop()
                else:
                    break
            stack.append((idx, current_node))
            results.append(0)
            idx += 1
            current_node = current_node.next
        return results


if __name__ == '__main__':
    test_input = linked_list_from_list([2, 1, 5])
    result = Solution().nextLargerNodes(test_input)
    print(result)

    test_input = linked_list_from_list([2, 7, 4, 3, 5])
    result = Solution().nextLargerNodes(test_input)
    print(result)
