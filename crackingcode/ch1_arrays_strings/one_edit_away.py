"""
One Away

There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings write a function to check they are one
edit (or zero edits) away.
"""


def one_edit_replace(first: str, second: str) -> bool:
    found_diff = False
    for idx, char in enumerate(first):
        other_char = second[idx]
        if char != other_char:
            if found_diff:
                return False
            found_diff = True
    return True


def one_edit_insert(first: str, second: str) -> bool:
    first_idx, second_idx = 0, 0
    while second_idx < len(second) and first_idx < len(first):
        if first[first_idx] != second[second_idx]:
            if first_idx != second_idx:
                return False
            second_idx += 1
        else:
            first_idx += 1
            second_idx += 1
    return True


def one_edit_away(first: str, second: str) -> bool:
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)
    return False


if __name__ == '__main__':
    assert one_edit_away("pale", "ple") is True
    assert one_edit_away("pales", "pale") is True
    assert one_edit_away("pale", "bale") is True
    assert one_edit_away("pale", "bae") is False
