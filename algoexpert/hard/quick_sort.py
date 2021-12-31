from typing import List


def quick_sort(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    pivot = array[0]
    smaller = []
    partition = [pivot]
    larger = []
    for idx in range(1, len(array)):
        if array[idx] < pivot:
            smaller.append(array[idx])
        elif array[idx] == pivot:
            partition.append(pivot)
        elif array[idx] > pivot:
            larger.append(array[idx])
    return quick_sort(smaller) + partition + quick_sort(larger)
