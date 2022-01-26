from typing import List


class Bst:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None


def in_order_traverse(root: Bst, values, key: int):
    if root is None:
        return
    in_order_traverse(root.left, values, key)
    if root.val != key:
        values.append(root.val)
    in_order_traverse(root.right, values, key)


def min_height_bst(array: List[int], start: int, end: int) -> Bst:
    if end < start:
        return
    middle = (start + end) // 2
    bst = Bst(array[middle])
    bst.left = min_height_bst(array, start, middle - 1)
    bst.right = min_height_bst(array, middle + 1, end)
    return bst


class BSTBucket:

    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Bst(key)
            return
        node = self.root
        while True:
            if key > node.val:
                if node.right is None:
                    node.right = Bst(key)
                    return
                else:
                    node = node.right
            elif key < node.val:
                if node.left is None:
                    node.left = Bst(key)
                    return
            else:
                return

    def remove(self, key):
        values = []
        in_order_traverse(self.root, values, key)
        if len(values) == 0:
            self.root = None
            return
        self.root = min_height_bst(values, 0, len(values) - 1)

    def __contains__(self, item):
        node = self.root
        while node:
            if item == node.val:
                return True
            elif item > node.val:
                node = node.right
            else:
                node = node.left
        return False


class MyHashSet:

    def __init__(self):
        self.bucket_count = 150_000
        self.buckets = []
        for i in range(self.bucket_count):
            self.buckets.append(BSTBucket())

    def add(self, key: int) -> None:
        bucket_idx = key % self.bucket_count
        self.buckets[bucket_idx].add(key)

    def remove(self, key: int) -> None:
        bucket_idx = key % self.bucket_count
        self.buckets[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = key % self.bucket_count
        return key in self.buckets[bucket_idx]
