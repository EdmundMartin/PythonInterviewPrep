class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        return "".join([s for s in s if s not in vowels])


if __name__ == "__main__":
    result = Solution().removeVowels("leetcodeisacommunityforcoders")
    assert result == "ltcdscmmntyfrcdrs"
