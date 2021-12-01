from typing import List


def sorted_squared_array(array: List[int]) -> List:
    result = [None for _ in range(len(array))]
    for idx, value in enumerate(array):
        new_value = value * value
        result[idx] = new_value
    result.sort()
    return result


if __name__ == '__main__':
    array = [1, 2, 3, 5, 6, 8, 9]
    solution = sorted_squared_array(array)
    assert solution == [1, 4, 9, 25, 36, 64, 81]
    assert array == [1, 2, 3, 5, 6, 8, 9]
