from typing import List


# Runtime: 96 ms, faster than 79.20% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.2 MB, less than 86.74% of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sorted_word = ''.join(sorted(word[::]))
            if sorted_word in results:
                results[sorted_word].append(word)
            else:
                results[sorted_word] = [word]
        return [value for value in results.values()]


if __name__ == '__main__':
    test_input = ["eat","tea","tan","ate","nat","bat"]
    output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result = Solution().groupAnagrams(test_input)
