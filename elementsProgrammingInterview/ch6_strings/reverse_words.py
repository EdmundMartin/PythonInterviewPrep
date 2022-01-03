from typing import List


def reverse_range(s: List[str], start: int, finish: int) -> None:
    while start < finish:
        s[start], s[finish] = s[finish], s[start]
        start, finish = start + 1, finish - 1


def reverse_words(s: List[str]) -> None:
    reverse_range(s, 0, len(s) - 1)

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != " ":
            finish += 1
        if finish == len(s):
            break
        reverse_range(s, start, finish - 1)
        start = finish + 1

    reverse_range(s, start, len(s) - 1)


if __name__ == "__main__":
    test_string = list("ram is costly")
    reverse_words(test_string)
    print("".join(test_string))
