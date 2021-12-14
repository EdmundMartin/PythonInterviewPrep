from typing import List


def swap(array: List[int], i: int, j: int) -> None:
    array[i], array[j] = array[j], array[i]


def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
    return array


if __name__ == '__main__':
    result = insertion_sort([24, 2, 242, 57, 243, 298, 56, 8, 9])
    assert result == [2, 8, 9, 24, 56, 57, 242, 243, 298]