from typing import List


# Runtime: 40 ms, faster than 84.02% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15 MB, less than 89.20% of Python3 online submissions for Fizz Buzz.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for i in range(1, n + 1):
            is_mod_5 = i % 5 == 0
            is_mod_3 = i % 3 == 0
            if is_mod_5 and is_mod_3:
                results.append("FizzBuzz")
            elif is_mod_5:
                results.append("Buzz")
            elif is_mod_3:
                results.append("Fizz")
            else:
                results.append(str(i))
        return results


if __name__ == "__main__":
    results = Solution().fizzBuzz(3)
    assert results == ["1", "2", "Fizz"]

    results = Solution().fizzBuzz(5)
    assert results == ["1", "2", "Fizz", "4", "Buzz"]
