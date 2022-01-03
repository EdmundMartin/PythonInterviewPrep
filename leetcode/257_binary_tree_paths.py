from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 32 ms, faster than 72.04% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 14.2 MB, less than 84.54% of Python3 online submissions for Binary Tree Paths.
class Solution:
    def clean_paths(self, paths: List[List[int]]):
        cleaned_paths = []
        for path in paths:
            cleaned_paths.append("->".join([str(s) for s in path]))
        return cleaned_paths

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        queue = [(root, [])]
        all_paths = []
        while queue:
            current_node, path_so_far = queue.pop(0)
            path_so_far = path_so_far[::]
            path_so_far.append(current_node.val)

            if not current_node.left and not current_node.right:
                all_paths.append(path_so_far)
            if current_node.left:
                queue.append((current_node.left, path_so_far))
            if current_node.right:
                queue.append((current_node.right, path_so_far))
        return self.clean_paths(all_paths)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    found_paths = Solution().binaryTreePaths(root)
    print(found_paths)
