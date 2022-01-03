from typing import List


class Trie:

    def __init__(self):
        self._trie = {}
        self._end = "END"

    def add_word(self, word: str):
        node = self._trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self._end] = word

    def prefix_in_trie(self, word: str):
        node = self._trie
        for ch in word:
            if ch in node:
                node = node[ch]
            else:
                return False, None
            if self._end in node:
                return True, node[self._end]
        return False, None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for item in dictionary:
            t.add_word(item)
        all_words = sentence.split(' ')
        for idx, word in enumerate(all_words):
            exists, replacement = t.prefix_in_trie(word)
            if exists:
                all_words[idx] = replacement
        return " ".join(all_words)


if __name__ == '__main__':
    res = Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
    print(res)

    res = Solution().replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs")
    print(res)