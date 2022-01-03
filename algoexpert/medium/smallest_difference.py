from typing import List


def smallest_difference(first: List[int], second: List[int]) -> List[int]:
    first.sort()
    second.sort()
    first_idx, second_idx = 0, 0
    smallest_diff = float("inf")
    current_pair = None
    while first_idx < len(first) and second_idx < len(second):
        difference = abs(first[first_idx] - second[second_idx])
        if difference < smallest_diff:
            current_pair = [first[first_idx], second[second_idx]]
            smallest_diff = difference
        if first[first_idx] < second[second_idx]:
            first_idx += 1
        elif first[first_idx] > second[second_idx]:
            second_idx += 1
        else:
            return current_pair
    return current_pair


if __name__ == "__main__":
    result = smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    assert result == [28, 26]
