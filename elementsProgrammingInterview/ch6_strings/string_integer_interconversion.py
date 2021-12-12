#Chapter 6.1
import functools
import string


def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] in '-+':], 0
    )


if __name__ == '__main__':
    result = string_to_int("110")
    print(result)