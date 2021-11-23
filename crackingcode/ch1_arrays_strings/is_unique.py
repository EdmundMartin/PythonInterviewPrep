"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use
additional data structures?

It's okay to assume 256 characters. This would be the case in extended ASCII. You should clarify your assumptions
with your interview.
"""


def is_unique(target: str) -> bool:
    if len(target) > 128:
        return False
    char_set = [False for _ in range(128)]
    for char in target:
        value = ord(char)
        if char_set[value]:
            return False
        char_set[value] = True
    return True


if __name__ == '__main__':
    unique_string = "aedfghjkl"
    duplicate_string = "abcdeabd"
    assert is_unique(unique_string) is True
    assert is_unique(duplicate_string) is False
