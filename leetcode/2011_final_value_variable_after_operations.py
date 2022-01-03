from typing import List


# Runtime: 40 ms, faster than 99.32% of Python3 online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 13.8 MB, less than 99.96% of Python3 online submissions for Final Value of Variable After Performing Operations.
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        while operations:
            operator = operations.pop()
            if operator[0] == "+" or operator[-1] == "+":
                value += 1
            else:
                value -= 1
        return value
