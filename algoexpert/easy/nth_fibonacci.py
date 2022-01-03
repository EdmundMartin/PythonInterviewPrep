def get_nth_fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)


if __name__ == "__main__":
    results = []
    for i in range(1, 10):
        results.append(get_nth_fibonacci(i))
    assert results == [0, 1, 1, 2, 3, 5, 8, 13, 21]
