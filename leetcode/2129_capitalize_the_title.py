

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        result = []
        for word in words:
            if len(word) > 2:
                new_word = word[0].upper() + word[1:].lower()
                result.append(new_word)
            else:
                result.append(word.lower())
        return " ".join(result)