from typing import List


def minimum_waiting_time(queries: List[int]) -> int:
    queries.sort()
    total_waiting_time = 0
    for idx, duration in enumerate(queries):
        queries_remaining = len(queries) - (idx + 1)
        total_waiting_time += queries_remaining * duration
    return total_waiting_time


if __name__ == '__main__':
    test_data = [3, 2, 1, 2, 6]
    result = minimum_waiting_time(test_data)
    assert result == 17
