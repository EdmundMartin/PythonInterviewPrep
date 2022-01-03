from typing import List


class Trie:

    def __init__(self):
        self._trie = {}
        self._end = "END"

    def insert(self, word):
        node = self._trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self._end] = word

    def words_beginning_with(self, chars: str):
        node = self._trie
        for ch in chars:
            if ch not in node:
                return []
            node = node[ch]
        words = []
        self._iterate_over_node(node, words)
        return sorted(words)

    def _iterate_over_node(self, node, words):
        for key in node.keys():
            if key == 'END':
                words.append(node[key])
            else:
                self._iterate_over_node(node[key], words)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        searched = []
        output = []
        for idx in range(1, len(searchWord) + 1):
            res = searchWord[0:idx]
            searched.append(res)
            prefix_result = trie.words_beginning_with(res)
            if len(prefix_result) > 3:
                prefix_result = prefix_result[:3]
            output.append(prefix_result)
        return output


if __name__ == '__main__':
    result = Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
    print(result[0])
    print(result[1])
    print(result[2])