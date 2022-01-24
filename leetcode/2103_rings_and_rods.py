

# Runtime: 32 ms, faster than 72.13% of Python3 online submissions for Rings and Rods.
# Memory Usage: 14.1 MB, less than 78.16% of Python3 online submissions for Rings and Rods.
class Solution:
    def countPoints(self, rings: str) -> int:
        mapping = {}
        contains_all = set()
        i = 0
        while i < len(rings):
            color = rings[i]
            idx = rings[i + 1]
            if idx in mapping:
                mapping[idx].add(color)
            else:
                mapping[idx] = {color}
            if len(mapping[idx]) == 3 and idx not in contains_all:
                contains_all.add(idx)
            i += 2
        return len(contains_all)


if __name__ == '__main__':
    count = Solution().countPoints("B0B6G0R6R0R6G9")
    assert count == 1

    count = Solution().countPoints("B0R0G0R9R0B0G0")
    assert count == 1

    count = Solution().countPoints("G4")
    assert count == 0
