# Chapter 6.2


def spreadsheet_encoding(col: str) -> int:
    result = 0
    for element in col:
        result = result * 26 + ord(element) - ord('A') + 1
    return result


if __name__ == '__main__':
    test = spreadsheet_encoding("ZZ")
    assert test == 702
