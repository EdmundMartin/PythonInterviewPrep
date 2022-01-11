from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        for change in gain:
            altitude += change
            max_altitude = max(altitude, max_altitude)
        return max_altitude


if __name__ == '__main__':
    test_array = [-5, 1, 5, 0, -7]
    result = Solution().largestAltitude(test_array)
    assert result == 1

    test_array = [-4, -3, -2, -1, 4, 3, 2]
    result = Solution().largestAltitude(test_array)
    assert result == 0
