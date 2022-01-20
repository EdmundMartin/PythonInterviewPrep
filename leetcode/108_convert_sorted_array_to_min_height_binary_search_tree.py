from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def construct_min_height_bst(self, array: List[int], start_idx: int, end_idx: int):
        if end_idx < start_idx:
            return
        middle_idx = (start_idx + end_idx) // 2
        root = TreeNode(array[middle_idx])
        root.left = self.construct_min_height_bst(array, start_idx, middle_idx - 1)
        root.right = self.construct_min_height_bst(array, middle_idx + 1, end_idx)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        return self.construct_min_height_bst(nums, 0, len(nums) - 1)