from typing import List


def three_number_sum(array: List[int], target_sum: int) -> List[List[int]]:
    array.sort()
    results = []
    for idx in range(len(array) - 2):
        left = idx + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[idx] + array[left] + array[right]
            if current_sum == target_sum:
                results.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
    return results


if __name__ == "__main__":
    found = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    assert found == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
