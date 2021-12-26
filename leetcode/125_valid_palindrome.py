from string import ascii_letters, digits


# Runtime: 44 ms, faster than 77.80% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.8 MB, less than 40.75% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        allowed_chars = set(ascii_letters + digits)
        for char in s:
            if char in allowed_chars:
                new_s += char
        return new_s == self.reverse_string(new_s)

    def reverse_string(self, s: str):
        as_list = list(s)
        i = 0
        j = len(as_list) - 1
        while i < j:
            as_list[i], as_list[j] = as_list[j], as_list[i]
            i += 1
            j -= 1
        return ''.join(as_list)


if __name__ == '__main__':
    test_one = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome(test_one) is True

    test_two = "race a car"
    assert Solution().isPalindrome(test_two) is False

    test_three = "  "
    assert Solution().isPalindrome(test_three) is True
