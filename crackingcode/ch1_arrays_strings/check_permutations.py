"""
Check Permutations

Given two strings, write a method to decide if one is a permutation of the other.
"""


def permutation_with_sort(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    return sorted(first) == sorted(second)


def permutation_char_counts(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    char_counts = [0 for _ in range(128)]  # Assumes ASCII
    for char in first:
        char_counts[ord(char)] += 1
    for char in second:
        char_counts[ord(char)] -= 1
        if char_counts[ord(char)] < 0:
            return False
    return True


if __name__ == '__main__':
    assert permutation_with_sort("dog", "god") is True
    assert permutation_with_sort("rita", "iitr") is False

    assert permutation_char_counts("dog", "god") is True
    assert permutation_char_counts("rita", "iitr") is False