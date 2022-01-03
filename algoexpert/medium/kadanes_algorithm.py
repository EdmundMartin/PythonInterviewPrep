from typing import List


def kadanes_algorithm(array: List[int]) -> int:
    current_sums = [0] * len(array)
    for idx, number in enumerate(array):
        if idx == 0:
            current_sums[0] = number
        else:
            new_sum = number + current_sums[idx - 1]
            current_sums[idx] = max(number, new_sum)
    return max(current_sums)


if __name__ == "__main__":
    result = kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])
    assert result == 19
