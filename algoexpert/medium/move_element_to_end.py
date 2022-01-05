from typing import List


def move_element_to_end(array: List[int], target: int) -> List[int]:
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] == target and array[j] != target:
            array[i], array[j] = array[j], array[i]
        if array[i] != target:
            i += 1
        if array[j] == target:
            j -= 1
    return array


if __name__ == '__main__':
    test_array = [2, 1, 2, 2, 2, 3, 4, 2]
    test_target = 2
    result = move_element_to_end(test_array, test_target)
    print(result)