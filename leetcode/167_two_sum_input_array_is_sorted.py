from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    result = Solution().twoSum(numbers, 9)
    assert result == [1, 2]

    numbers = [2, 3, 4]
    target = 6
    result = Solution().twoSum(numbers, target)
    assert result == [1, 3]

    numbers = [-1, 0]
    target = -1
    result = Solution().twoSum(numbers, target)
    assert result == [1, 2]
