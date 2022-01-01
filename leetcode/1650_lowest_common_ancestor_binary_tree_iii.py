

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        results = {}
        while p:
            results[p.val] = p
            p = p.parent
        while q:
            if q.val in results:
                return results[q.val]
            q = q.parent
