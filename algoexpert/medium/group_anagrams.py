from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    results = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in results:
            results[sorted_word].append(word)
        else:
            results[sorted_word] = [word]
    output = []
    for value in results.values():
        output.append(value)
    return output


if __name__ == '__main__':
    test_words = ["yo", "oy", "act", "tac"]
    result = group_anagrams(test_words)
    assert result == [["yo", "oy"], ["act", "tac"]]