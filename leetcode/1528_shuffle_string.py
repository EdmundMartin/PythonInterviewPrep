from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [None] * len(s)
        for zipped in zip(s, indices):
            output[zipped[1]] = zipped[0]
        return "".join(output)


if __name__ == "__main__":
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    result = Solution().restoreString(s, indices)
    print(result)
