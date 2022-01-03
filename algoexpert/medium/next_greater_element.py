from typing import List


def next_greater_element(array: List[int]) -> List[int]:
    result = [-1] * len(array)
    stack = []

    for idx in range(2 * len(array)):
        real_idx = idx % len(array)

        while len(stack) > 0 and array[stack[-1]] < array[real_idx]:
            top = stack.pop()
            result[top] = array[real_idx]

        stack.append(real_idx)

    return result
