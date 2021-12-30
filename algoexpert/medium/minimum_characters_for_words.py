from typing import List


def minimum_characters_for_words(words: List[str]) -> List[str]:
    counts = {}
    for word in words:
        word_count = {}
        for ch in word:
            if ch in word_count:
                word_count[ch] += 1
            else:
                word_count[ch] = 1
        for key, value in word_count.items():
            if key in counts:
                counts[key] = max(counts[key], value)
            else:
                counts[key] = value
    output = []
    for key, value in counts.items():
        for i in range(value):
            output.append(key)
    return output
