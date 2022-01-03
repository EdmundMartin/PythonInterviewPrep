class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        all_jewels = set(jewels)
        count = 0
        for stone in stones:
            if stone in all_jewels:
                count += 1
        return count
