def compress(target: str) -> str:
    compressed = ""
    count_repeating = 0

    for idx in range(len(target)):
        count_repeating += 1

        if idx + 1 >= len(target) or target[idx] != target[idx + 1]:
            compressed += f"{target[idx]}{count_repeating}"
            count_repeating = 0
    if len(compressed) < len(target):
        return compressed
    return target


if __name__ == "__main__":
    test_string = "eeeddddaaaabcd"
    result = compress(test_string)
    assert result == "e3d4a4b1c1d1"
