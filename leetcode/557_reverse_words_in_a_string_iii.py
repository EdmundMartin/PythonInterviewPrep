from typing import List, Any


def reverse_in_place(array: List[Any]):
    i = 0
    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        words = s.split(" ")
        for word in words:
            word_list = list(word)
            reverse_in_place(word_list)
            result.append("".join(word_list))
        return "".join(result)
