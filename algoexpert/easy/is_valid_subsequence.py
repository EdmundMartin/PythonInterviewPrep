from typing import List


def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
    if len(sequence) > len(array):
        return False
    idx = 0
    for value in array:
        if value == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True
    return False


if __name__ == "__main__":
    result = is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    assert result is True
