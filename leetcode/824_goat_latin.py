

# Runtime: 28 ms, faster than 82.86% of Python3 online submissions for Goat Latin.
# Memory Usage: 14.4 MB, less than 15.00% of Python3 online submissions for Goat Latin.
class Solution:

    def split_sentence(self, sentence: str):
        output = []
        current_word = ""
        for char in sentence:
            if char == " ":
                if len(current_word) > 0:
                    output.append(current_word)
                current_word = ""
            else:
                current_word += char
        if len(current_word) > 0:
            output.append(current_word)
        return output

    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        words = self.split_sentence(sentence)
        output = []
        for idx, word in enumerate(words):
            if word[0].lower() in vowels:
                goat_vocab = word + "ma"
            else:
                new_ending = word[0] + "ma"
                goat_vocab = word[1:] + new_ending
            goat_whine = "a" * (idx + 1)
            goat_vocab = goat_vocab + goat_whine
            output.append(goat_vocab)
        return " ".join(output)


if __name__ == '__main__':
    result = Solution().toGoatLatin("I speak Goat Latin")
    assert result == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    result = Solution().toGoatLatin("The quick brown fox jumped over the lazy dog")
    assert result == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
