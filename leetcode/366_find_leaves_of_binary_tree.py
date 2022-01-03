from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, parent, is_left):
        self.parent = parent
        self.is_left = is_left


# Runtime: 24 ms, faster than 96.51% of Python3 online submissions for Find Leaves of Binary Tree.
# Memory Usage: 14.3 MB, less than 59.07% of Python3 online submissions for Find Leaves of Binary Tree.
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        all_levels = []
        while root:
            queue = [(root, TreeInfo(None, None))]
            results = []
            while queue:
                current_node, info = queue.pop(0)
                if not current_node.left and not current_node.right:
                    if info.parent is None:
                        root = None
                    else:
                        if info.is_left:
                            info.parent.left = None
                        else:
                            info.parent.right = None
                    results.append(current_node.val)
                if current_node.left:
                    queue.append((current_node.left, TreeInfo(current_node, True)))
                if current_node.right:
                    queue.append((current_node.right, TreeInfo(current_node, False)))
            all_levels.append(results)
        return all_levels


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = Solution().findLeaves(root)
    print(result)
