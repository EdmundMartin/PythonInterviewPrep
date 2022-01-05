from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_tree(array: List[int]):
    if len(array) == 0:
        return
    max_value = max(array)
    max_idx = array.index(max_value)
    bst = TreeNode(max_value)
    bst.left = max_tree(array[:max_idx])
    bst.right = max_tree(array[max_idx + 1:])
    return bst


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return max_tree(nums)


if __name__ == '__main__':
    test_nums = [3, 2, 1, 6, 0, 5]

    root = Solution().constructMaximumBinaryTree(test_nums)
    print(root.val)
    print(root.right.val)
    print(root.right.left.val)