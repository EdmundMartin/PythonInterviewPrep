from typing import List


def selection_sort(array: List[int]) -> List[int]:
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        array[current_idx], array[smallest_idx] = array[smallest_idx], array[current_idx]
        current_idx += 1
    return array


if __name__ == '__main__':
    result = selection_sort([10, 27, 7, 8, 3, 5, 4, 6])
    assert result == [3, 4, 5, 6, 7, 8, 10, 27]
