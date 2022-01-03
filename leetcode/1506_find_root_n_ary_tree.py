from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# Runtime: 140 ms, faster than 85.54% of Python3 online submissions for Find Root of N-Ary Tree.
# Memory Usage: 24.9 MB, less than 50.00% of Python3 online submissions for Find Root of N-Ary Tree.
class Solution:
    def findRoot(self, tree: List["Node"]) -> "Node":
        no_children = {}
        is_child = set()
        for node in tree:
            if node.val not in is_child:
                no_children[node.val] = node
            for child in node.children:
                if child.val in no_children:
                    del no_children[child.val]
                is_child.add(child.val)
        return list(no_children.values())[0]
