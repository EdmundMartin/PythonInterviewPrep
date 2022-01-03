

# Runtime: 181 ms, faster than 58.35% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.7 MB, less than 90.88% of Python3 online submissions for Implement Trie (Prefix Tree).
class Trie:

    def __init__(self):
        self._trie = {}
        self._end = 'END'

    def insert(self, word: str) -> None:
        node = self._trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self._end] = "*"

    def search(self, word: str) -> bool:
        node = self._trie
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self._end in node

    def startsWith(self, word: str) -> bool:
        node = self._trie
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    result = trie.search("apple")
    assert result is True
    result = trie.search("app")
    assert result is False
    result = trie.startsWith("app")
    assert result is True
    trie.insert("app")
    result = trie.search("app")
    assert result is True