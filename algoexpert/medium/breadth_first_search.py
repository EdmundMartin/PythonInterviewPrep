from typing import List


class GraphNode:
    def __init__(self, name: str):
        self.name = name
        self.children: List["GraphNode"] = []

    def add_child(self, name: str) -> "GraphNode":
        self.children.append(GraphNode(name))
        return self

    def breadth_first_search(self, array: List[str]):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
