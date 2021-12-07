

def encoding(s: str) -> str:
    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            result.append(f'{count}{s[i - 1]}')
            count = 1
        else:
            count += 1
    return ''.join(result)


def decoding(s: str) -> str:
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = (count * 10) + int(c)
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)


if __name__ == '__main__':
    test_string = "eeedmunnnddd"
    result = encoding(test_string)
    assert result == "3e1d1m1u3n3d"
    final = decoding(result)
    assert final == "eeedmunnnddd"
