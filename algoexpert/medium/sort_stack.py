from typing import List


def sort_stack(stack: List[int]) -> List[int]:
    if len(stack) == 0:
        return stack
    top = stack.pop()

    sort_stack(stack)

    insert_sorted_order(stack, top)

    return stack


def insert_sorted_order(stack, value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()

    insert_sorted_order(stack, value)

    stack.append(top)


if __name__ == "__main__":
    test_array = [-4, 3, 5, 7, 2, 1, 8]
    result = sort_stack(test_array)
    assert result == [-4, 1, 2, 3, 5, 7, 8]
