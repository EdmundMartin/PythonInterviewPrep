from typing import List


def helper(array: List[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    middle = (left + right) // 2
    if target == array[middle]:
        return middle
    elif target > array[middle]:
        return helper(array, target, middle + 1, right)
    else:
        return helper(array, target, left, middle - 1)


def binary_search(array: List[int], target: int) -> int:
    return helper(array, target, 0, len(array)-1)


if __name__ == '__main__':
    test_array = [0, 1, 21, 33, 45, 61, 71, 72, 73]
    test_target = 33
    result = binary_search(test_array, test_target)
    print(result)