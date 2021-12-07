

def roman_to_int(value: str) -> int:
    value = value.upper()
    sum = 0
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(value)):
        try:
            int_value = nums[value[i]]
            if i + 1 < len(value) and nums[value[i + 1]] > int_value:
                sum -= int_value
            else:
                sum += int_value
        except KeyError:
            raise ValueError("Invalid roman numeral")
    return sum


if __name__ == '__main__':
    result = roman_to_int("XLII")
    assert result == 42