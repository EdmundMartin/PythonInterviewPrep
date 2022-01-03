

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            steps += 1
        return steps


if __name__ == '__main__':
    result = Solution().numberOfSteps(14)
    print(result)

    result = Solution().numberOfSteps(8)
    print(result)

    result = Solution().numberOfSteps(123)
    print(result)