class ArrayReader:
    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        if index >= len(self.array):
            return 2 ** 31 - 1
        return self.array[index]


class Solution:
    def search(self, reader, target):

        left = 0
        right = 10 ** 4 + 1

        while left <= right:
            middle = left + (right - left) // 2
            if reader.get(middle) < target:
                left = middle + 1
            if reader.get(middle) > target:
                right = middle - 1
            elif reader.get(middle) == target:
                return middle
        return -1


if __name__ == "__main__":
    res = ArrayReader([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    resul = Solution().search(res, 5)
