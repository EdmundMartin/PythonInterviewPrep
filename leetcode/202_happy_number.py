

class Solution:

    def isHappy(self, n: int):
        n_str = str(n)
        seen = set()
        while True:
            current_sum = 0
            for char in n_str:
                current_sum += int(char) * int(char)
            if current_sum == 1:
                return True
            if current_sum in seen:
                return False
            seen.add(current_sum)
            n_str = str(current_sum)


if __name__ == '__main__':
    result = Solution().isHappy(19)
    assert result is True

    result = Solution().isHappy(2)
    assert result is False