from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 48 ms, faster than 77.35% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.4 MB, less than 97.86% of Python3 online submissions for Average of Levels in Binary Tree.
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        queue = [(root, 0)]
        while queue:
            current_node, level = queue.pop(0)
            if level == len(levels):
                levels.append([current_node.val])
            else:
                levels[level].append(current_node.val)
            if current_node.left:
                queue.append((current_node.left, level +1))
            if current_node.right:
                queue.append((current_node.right, level + 1))
        squashed_levels = []
        for level in levels:
            squashed_levels.append(sum(level) / len(level))
        return squashed_levels


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().averageOfLevels(root)
    print(result)