from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Faster than 70%
class SolutionIterative:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        if not root:
            return None
        copied_nodes = {}
        stack = [root]

        while stack:
            node = stack.pop()
            copied_nodes[node] = NodeCopy(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        for_copying = [root]
        while for_copying:
            node = for_copying.pop()
            copied = copied_nodes[node]
            if node.left:
                copied.left = copied_nodes[node.left]
                for_copying.append(node.left)
            if node.right:
                copied.right = copied_nodes[node.right]
                for_copying.append(node.right)
            if node.random:
                copied.random = copied_nodes[node.random]

        return copied_nodes[root]


# Very slow
class Solution:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:

        node_copies = {}

        def depth_first_search(root):
            if not root:
                return
            if root in node_copies:
                return node_copies[root]
            copied_root = NodeCopy(root.val)
            node_copies[root] = copied_root
            copied_root.left = depth_first_search(root.left)
            copied_root.right = depth_first_search(root.right)
            copied_root.random = depth_first_search(root.random)
            return copied_root

        return depth_first_search(root)
