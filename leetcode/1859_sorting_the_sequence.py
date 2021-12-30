

# Runtime: 45 ms, faster than 9.88% of Python3 online submissions for Sorting the Sentence.
# Memory Usage: 14 MB, less than 98.61% of Python3 online submissions for Sorting the Sentence.
class Solution:
    def sortSentence(self, s: str) -> str:
        split_sentence = s.split(' ')
        word_count = len(split_sentence)
        indexes = [None] * word_count
        for sentence in split_sentence:
            idx = int(sentence[-1])
            indexes[idx - 1] = sentence[:-1]
        return ' '.join(indexes)


if __name__ == '__main__':
    result = Solution().sortSentence("is2 sentence4 This1 a3")
    assert result == "This is a sentence"
