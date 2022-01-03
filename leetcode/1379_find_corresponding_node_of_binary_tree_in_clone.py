class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 624 ms, faster than 67.90% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 24.2 MB, less than 49.93% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        correct_path = []

        queue = [(original, [])]
        while queue:
            node, path = queue.pop(0)
            path = path[::]
            if node.val == target.val:
                correct_path = path
                break
            if node.left:
                path.append("left")
                queue.append((node.left, path))
            if node.right:
                path.append("right")
                queue.append((node.right, path))

        while correct_path:
            path_direction = correct_path.pop(0)
            if path_direction == "left":
                cloned = cloned.left
            else:
                cloned = cloned.right

        return cloned
