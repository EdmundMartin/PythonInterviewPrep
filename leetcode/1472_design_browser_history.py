
class DoubleLinkedNode:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = DoubleLinkedNode(homepage)

    def visit(self, url: str) -> None:
        node = DoubleLinkedNode(url)
        self.node.next = node
        node.prev = self.node
        self.node = node

    def back(self, steps: int) -> str:
        current_node = self.node
        k = 0
        while current_node.prev and k < steps:
            current_node = current_node.prev
            k += 1
        self.node = current_node
        return current_node.value

    def forward(self, steps:int) -> str:
        current_node = self.node
        k = 0
        while current_node.next and k < steps:
            current_node = current_node.next
            k += 1
        self.node = current_node
        return current_node.value


if __name__ == '__main__':
    history = BrowserHistory("leetcode.com")
    history.visit("google.com")
    history.visit("facebook.com")
    history.visit("youtube.com")
    result = history.back(1)
    assert result == "facebook.com"
    result = history.back(1)
    assert result == "google.com"
    result = history.forward(1)
    assert result == "facebook.com"
    history.visit("linkedin.com")
    result = history.forward(2)
    assert result == "linkedin.com"
    result = history.back(2)
    assert result == "google.com"
    result = history.back(7)
    assert result == "leetcode.com"