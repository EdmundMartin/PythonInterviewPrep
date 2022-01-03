from collections import defaultdict


def generate_document(characters: str, document: str) -> bool:
    char_map = defaultdict(int)
    for char in characters:
        char_map[char] += 1
    for char in document:
        count = char_map[char]
        if count == 0:
            return False
        char_map[char] -= 1
    return True


if __name__ == "__main__":
    test_document = "Edmund Martin"
    test_chars_true = "dmundE artinM"
    test_chars_false = "dmunde artin"
    assert generate_document(test_chars_true, test_document) is True
    assert generate_document(test_chars_false, test_document) is False
