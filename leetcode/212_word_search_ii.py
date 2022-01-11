from typing import List


class TrieNode:
    def __init__(self):
        self.edges = dict()
        self.end = False

    def add(self, word):
        node = self

        for char in word:
            if char not in node.edges:
                node.edges[char] = TrieNode()
            node = node.edges[char]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        words_found = set()

        max_row = len(board)
        max_col = len(board[0])

        trie = TrieNode()
        for word in words:
            trie.add(word)

        def find_words(row, col):

            visited = set()

            def dfs(row, col, prefix, trie_node):
                words_found.add(prefix)
                visited.add((row, col))

                new_node = trie_node.edges[board[row][col]]

                for new_row, new_col in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ]:
                    if (
                        new_row >= 0
                        and new_row < max_row
                        and new_col >= 0
                        and new_col < max_col
                        and (new_row, new_col) not in visited
                    ):
                        if board[new_row][new_col] in new_node.edges:
                            next_prefix = prefix + board[new_row][new_col]
                            dfs(new_row, new_col, next_prefix, new_node)

                visited.remove((row, col))

            dfs(row, col, board[row][col], trie)

        for r in range(max_row):
            for c in range(max_col):
                if board[r][c] in trie.edges:
                    find_words(r, c)

        return list(words_found & words)
