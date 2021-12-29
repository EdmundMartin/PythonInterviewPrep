from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_height = float('-inf')
        max_idx = None
        for i in range(1, len(arr) - 1):
            peak = arr[i]
            if peak > arr[i - 1] and peak > arr[i + 1]:
                if peak > max_height:
                    max_height = peak
                    max_idx = i
        return max_idx


if __name__ == '__main__':
    result = Solution().peakIndexInMountainArray([0, 1, 0])
    print(result)