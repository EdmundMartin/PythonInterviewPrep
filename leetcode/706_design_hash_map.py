from typing import Tuple, List


class Node:

    def __init__(self):
        self.values: List[Tuple[int, int]] = []

    def contains(self, key: int) -> Tuple[bool, int]:
        for idx, pair in enumerate(self.values):
            k, v = pair
            if key == k:
                return True, idx
        return False, -1

    def update(self, key: int, value: int):
        contained, idx = self.contains(key)
        if not contained:
            self.values.append((key, value))
        self.values[idx] = (key, value)

    def retrieve(self, key: int):
        contained, idx = self.contains(key)
        if not contained:
            return -1
        return self.values[idx][1]

    def remove(self, key: int):
        contained, idx = self.contains(key)
        if not contained:
            return
        self.values.pop(idx)


class MyHashMap:

    def __init__(self):
        self.size = 3_500
        self.nodes: List[Node] = []
        for i in range(self.size):
            self.nodes.append(Node())

    def put(self, key: int, value: int) -> None:
        idx = hash(key) % self.size
        self.nodes[idx].update(key, value)

    def get(self, key: int) -> int:
        idx = hash(key) % self.size
        return self.nodes[idx].retrieve(key)

    def remove(self, key: int) -> None:
        idx = hash(key) % self.size
        self.nodes[idx].remove(key)
