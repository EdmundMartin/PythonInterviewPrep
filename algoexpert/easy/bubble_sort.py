from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    loops = len(array)
    while loops > 0:
        swaps = 0
        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                swaps += 1
        if swaps == 0:
            break
        loops -= 1
    return array


if __name__ == '__main__':
    result = bubble_sort([11, 2, 4, 8, 9, 3, 1, 1, 139, 273, 15])
    assert result == [1, 1, 2, 3, 4, 8, 9, 11, 15, 139, 273]