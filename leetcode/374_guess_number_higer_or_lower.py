# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


def guess(num: int) -> int:
    ...


class Solution:

    def binary_search(self, left, right):
        middle = (left + right) // 2
        result = guess(middle)
        if result == -1:
            return self.binary_search(left, middle - 1)
        elif result == 1:
            return self.binary_search(middle + 1, right)
        else:
            return middle

    def guessNumber(self, n: int) -> int:
        return self.binary_search(1, n)