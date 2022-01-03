def is_palindrome(target: str) -> bool:
    back_idx = len(target) - 1
    for forward_idx, _ in enumerate(target):
        if target[forward_idx] != target[back_idx]:
            return False
        if forward_idx >= back_idx:
            return True
        back_idx -= 1


if __name__ == "__main__":
    assert is_palindrome("tat") is True
    assert is_palindrome("bobobs") is False
