from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for idx, value in enumerate(groupSizes):
            if value not in groups:
                groups[value] = [idx]
            else:
                groups[value].append(idx)
        results = []
        for key, value in groups.items():
            if len(value) == key:
                results.append(value)
            else:
                while len(value):
                    group, value = value[:key], value[key:]
                    results.append(group)
        return results


# Runtime: 67 ms, faster than 97.03% of Python3 online submissions for Group the People Given the Group Size They Belong To.
# Memory Usage: 14.3 MB, less than 71.32% of Python3 online submissions for Group the People Given the Group Size They Belong To.
class SolutionFaster:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        results = []
        for idx, value in enumerate(groupSizes):
            if value not in groups:
                groups[value] = [idx]
            else:
                groups[value].append(idx)
            if len(groups[value]) == value:
                results.append(groups[value])
                groups[value] = []
        return results


if __name__ == "__main__":
    group_sizes = [3, 3, 3, 3, 3, 1, 3]
    result = Solution().groupThePeople(group_sizes)
    print(result)
