from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count


class OtherSolution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        sub_patterns = set()
        for i in range(len(word)):
            for j in range(1, len(word) + 1):
                if len(word[i:j]) > 0:
                    sub_patterns.add(word[i:j])
        count = 0
        for pattern in patterns:
            if pattern in sub_patterns:
                count += 1
        return count


if __name__ == '__main__':
    result = OtherSolution().numOfStrings(["a", "abc", "bc", "d"], "abc")
    print(result)