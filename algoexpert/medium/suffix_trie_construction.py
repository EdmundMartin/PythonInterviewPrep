class SuffixTrie:
    def __init__(self, string: str):
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_trie(string)

    def populate_suffix_trie(self, string: str):
        for i in range(len(string)):
            self.insert_substring_at(i, string)

    def insert_substring_at(self, i: int, string: str):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True

    def contains(self, item: str):
        node = self.root
        for letter in item:
            if letter not in node:
                return False
            node = node[letter]
        return self.end_symbol in node
