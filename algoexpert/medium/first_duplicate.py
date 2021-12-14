from typing import List


def first_duplicate_two_pointers(array: List[int]) -> int:
    min_second_idx = len(array)

    for idx, value in enumerate(array):
        for j in range(idx + 1, len(array)):
            if value == array[j]:
                min_second_idx = min(min_second_idx, j)

    if min_second_idx == len(array):
        return -1

    return array[min_second_idx]


def first_duplicate_using_set(array: List[int]) -> int:
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


if __name__ == '__main__':
    first_variant = first_duplicate_two_pointers([2, 1, 5, 2, 3, 3, 4])
    second_variant = first_duplicate_using_set([2, 1, 5, 2, 3, 3, 4])

    assert first_variant == 2
    assert second_variant == 2
