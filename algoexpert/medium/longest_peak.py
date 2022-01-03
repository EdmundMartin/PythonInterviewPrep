from typing import List


def measure_peak(array: List[int], start_idx: int):
    size = 1
    prev = array[start_idx]
    back_idx = start_idx
    front_idx = start_idx
    while back_idx > 0 and array[back_idx - 1] < prev:
        size += 1
        prev = array[back_idx - 1]
        back_idx -= 1
    prev = array[start_idx]
    while front_idx < len(array) - 1 and array[front_idx + 1] < prev:
        size += 1
        prev = array[front_idx + 1]
        front_idx += 1
    return size


def longest_peak(array: List[int]) -> int:
    peaks = []
    for idx, value in enumerate(array):
        if idx == 0 or idx == len(array) - 1:
            continue
        if value > array[idx - 1] and array[idx + 1] < value:
            peaks.append(idx)
    longest = float("-inf")
    for peak in peaks:
        longest = max(measure_peak(array, peak), longest)
    return longest


if __name__ == "__main__":
    result = longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
    assert result == 6
