def is_palindrome(s: str) -> bool:
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == "__main__":
    palindrome = is_palindrome("mom")
    assert palindrome is True

    not_palindrome = is_palindrome("edmund")
    assert not_palindrome is False
