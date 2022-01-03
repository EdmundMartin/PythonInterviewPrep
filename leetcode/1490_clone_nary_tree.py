class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = self.children if children is not None else []


class Solution:
    def cloneTree(self, root: Node) -> Node:
        if not root:
            return

        copy = Node(root.val)

        def pre_order(node: "Node", copy: "Node"):
            if not node:
                return

            for idx, child in enumerate(node.children):
                new_child = Node(child.val)
                copy.children.append(new_child)
                pre_order(node.children[idx], new_child)

        pre_order(root, copy)
        return copy
