from typing import List


def get_next_idx(array: List[int], current_idx: int) -> int:
    jump_size = array[current_idx]
    next_idx = (current_idx + jump_size) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


def has_single_cycle(array: List) -> bool:
    num_elements_visited = 0
    idx = 0
    while num_elements_visited < len(array):
        if num_elements_visited > 0 and idx == 0:
            return False
        num_elements_visited += 1
        idx = get_next_idx(array, idx)
    return idx == 0
