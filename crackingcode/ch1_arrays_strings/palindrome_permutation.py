from typing import Dict
from collections import defaultdict


def build_freq_table(phrase: str) -> Dict[str, int]:
    counter = defaultdict(int)
    for char in phrase:
        if char == " ":
            continue
        counter[char] += 1
    return counter


def check_max_one_odd(counter: Dict[str, int]) -> bool:
    found_odd = False
    for value in counter.values():
        if value % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def palindrome_permutation_hash_table(phrase: str) -> bool:
    counter = build_freq_table(phrase)
    return check_max_one_odd(counter)


def get_char_value(char: str) -> int:
    a = ord("a")
    z = ord("z")
    val = ord(char)
    if a <= val <= z:
        return val - a
    return -1


def palindrome_permutation_optimized(phrase: str) -> bool:
    count_odd = 0
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    for char in phrase:
        char_num = get_char_value(char)
        if char_num != -1:
            table[char_num] += 1
            if table[char_num] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd <= 1


if __name__ == "__main__":
    assert palindrome_permutation_hash_table("tact coa") is True
    assert palindrome_permutation_hash_table("edmund martin") is False

    assert palindrome_permutation_optimized("tact coa") is True
    assert palindrome_permutation_optimized("edmund martin") is False
