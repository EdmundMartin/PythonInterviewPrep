def run_length_encoding(target_str: str):
    new_string = ""
    prev = target_str[0]
    count = 1
    for current in target_str[1:]:
        if current != prev:
            new_string += f"{prev}{count}"
            count = 0
        if count == 9:
            new_string += f"{prev}{count}"
            count = 0
        prev = current
        count += 1
    new_string += f"{prev}{count}"
    return new_string


if __name__ == "__main__":
    test_str: str = "AAAAAAAAAAAAAAAAAAAAAHHHHCCCCDDDDPPPSL"
    result = run_length_encoding(test_str)
    print(result)
