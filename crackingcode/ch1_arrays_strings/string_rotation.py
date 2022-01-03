"""
String: Rotation
Assume you have a method is_sub_string
which checks if one word is a sub_string of another.

With only one call to substring, check if s2 is a rotation of s1.
"""


def is_substring(first: str, second: str) -> bool:
    return second in first


def is_rotation(first: str, second: str) -> bool:
    length = len(first)

    if length == len(second) and length > 0:
        first_modified = first + first
        return is_substring(first_modified, second)
    return False


if __name__ == "__main__":
    original = "waterbottle"
    rotation = "erbottlewat"
    assert is_rotation(original, rotation) is True
