

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(' ')
        last = float('-inf')
        for word in words:
            if word.isdigit():
                if int(word) <= last:
                    return False
                else:
                    last = int(word)
        return True
