from typing import List


def three_largest_numbers(array: List[int]) -> List[int]:
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for value in array:
        if value > first:
            first, second, third = value, first, second
        elif value > second:
            second, third = value, second
        elif value > third:
            third = value

    return [third, second, first]


if __name__ == '__main__':
    result = three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
    assert result == [18, 141, 541]