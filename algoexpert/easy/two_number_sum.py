from typing import List


def two_sum(array: List[int], target_sum: int) -> List[int]:
    seen = set()
    for num in array:
        other = target_sum - num
        if other in seen:
            return [other, num]
        seen.add(num)
    return []


if __name__ == '__main__':
    test_array: List[int] = [3, 5, -4, 8, 11, 1, -1, 6]
    test_target: int = 10
    result = two_sum(test_array, test_target)
    assert result == [11, -1]