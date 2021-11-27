

def caesar_cipher(target: str, key: int) -> str:
    cipher = ""
    if key > 26:
        key = key % 26
    for letter in target:
        if ord(letter) + key > 122:
            diff = (122 - ord(letter)) + 1
            cipher += chr(diff)
        else:
            cipher += chr(ord(letter) + key)
    return cipher


if __name__ == '__main__':
    result = caesar_cipher("edmund", 3)
    assert result == "hgpxqg"