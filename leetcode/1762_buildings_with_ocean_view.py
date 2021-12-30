from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = [len(heights) - 1]
        idx = len(heights) - 2
        max_height = heights[len(heights) - 1]
        while idx >= 0:
            if heights[idx] > max_height:
                output.insert(0, idx)
                max_height = heights[idx]
            idx -= 1
        return output
