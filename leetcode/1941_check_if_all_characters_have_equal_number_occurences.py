

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        return len(set(counter.values())) == 1
