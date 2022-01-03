from collections import defaultdict


# return index of first non repeating char
def first_non_repeating_char(target: str) -> int:
    counter = defaultdict(int)
    for char in target:
        counter[char] += 1
    for idx, char in enumerate(target):
        if counter[char] == 1:
            return idx
    return -1


if __name__ == "__main__":
    test_str: str = "abcdcaf"
    result = first_non_repeating_char(test_str)
    assert 1 == result
