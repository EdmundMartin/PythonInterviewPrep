from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairings = {}
        for pair in similarPairs:
            key_one, key_two = pair
            if key_one in pairings:
                pairings[key_one].add(key_two)
            else:
                pairings[key_one] = {key_two}
            if key_two in pairings:
                pairings[key_two].add(key_one)
            else:
                pairings[key_two] = {key_one}

        for idx in range(len(sentence1)):
            if sentence1[idx] == sentence2[idx]:
                continue
            value = pairings.get(sentence1[idx], set())
            if sentence2[idx] not in value:
                return False
        return True


if __name__ == '__main__':
    sent_one = ["great", "acting", "skills"]
    sent_two = ["fine", "drama", "talent"]
    pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]

    result = Solution().areSentencesSimilar(sent_one, sent_two, pairs)
    assert result is True
