from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        pairs = []
        for idx, number in enumerate(nums):
            if number not in seen:
                seen[number] = [idx]
            else:
                other_idxs = seen[number]
                for other in other_idxs:
                    pairs.append((other, idx))
                seen[number].append(idx)
        return len(pairs)


if __name__ == '__main__':
    result = Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3])
    assert result == 4

    result = Solution().numIdenticalPairs([1, 1, 1, 1])
    assert result == 6

    result = Solution().numIdenticalPairs([1, 2, 3])
    assert result == 0