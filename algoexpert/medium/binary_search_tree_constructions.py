from typing import Optional


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["BST"] = None
        self.right: Optional["BST"] = None

    def insert(self, value: int) -> "BST":
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self

    def contains(self, value: int) -> bool:
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def get_min_value(self) -> int:
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def remove(self, value: int, parent_node: Optional["BST"] = None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                # we are going to come back to this root node case
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        current_node.value = None
                elif parent_node.left == current_node:
                    parent_node.left = (
                        current_node.left
                        if current_node.left is not None
                        else current_node.right
                    )
                elif parent_node.right == current_node:
                    parent_node.right = (
                        current_node.left
                        if current_node.left is not None
                        else current_node.right
                    )
                break
        return self
