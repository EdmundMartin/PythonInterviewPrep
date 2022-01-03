from typing import List


class Node:
    def __init__(self, name: str):
        self.children: List["Node"] = []
        self.name = name

    def add_child(self, name) -> "Node":
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array: List[str]) -> List[str]:
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
