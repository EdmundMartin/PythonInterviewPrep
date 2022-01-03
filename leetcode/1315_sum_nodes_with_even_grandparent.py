class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        queue = [(root, [])]
        sum = 0
        while queue:
            node, family = queue.pop(0)
            if len(family) == 2 and family[0] % 2 == 0:
                sum += node.val

            if node.left:
                left_family = family[::]
                left_family.append(node.val)
                if len(left_family) > 2:
                    left_family.pop(0)
                queue.append((node.left, left_family))
            if node.right:
                right_family = family[::]
                right_family.append(node.val)
                if len(right_family) > 2:
                    right_family.pop(0)
                queue.append((node.right, right_family))
        return sum
