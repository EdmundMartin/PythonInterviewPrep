from typing import List


def reverse_range(contents: List[str], start: int, end: int):
    while start < end:
        contents[start], contents[end] = contents[end], contents[start]
        start += 1
        end -= 1


def reverse_words_in_string(string: str) -> str:
    characters = list(string)
    reverse_range(characters, 0, len(characters) - 1)

    start_word = 0
    while start_word < len(characters):
        end_word = start_word
        while end_word < len(characters) and characters[end_word] != " ":
            end_word += 1

        reverse_range(characters, start_word, end_word - 1)
        start_word = end_word + 1

    return "".join(characters)


if __name__ == '__main__':
    result = reverse_words_in_string("edmund is the best")
    assert result == "best the is edmund"
