from typing import List


def product_sum(array: List[int], depth: int = 1):
    prod_sum = 0
    for value in array:
        if isinstance(value, list):
            prod_sum += product_sum(value, depth + 1)
        else:
            prod_sum += value
    return prod_sum * depth


if __name__ == '__main__':
    test_data = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    result = product_sum(test_data)
    assert result == 12
