from collections import defaultdict


class SolutionToSlow:

    def contains_characters_for_number(self, s: dict, target):
        return all([t in s for t in target])

    def originalDigits(self, s: str) -> str:
        digits_as_text = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        result = []
        char_dict = {}
        for ch in s:
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1
        while len(char_dict) > 0:
            for digit in digits_as_text.keys():
                if self.contains_characters_for_number(char_dict, digit):
                    result.append(digits_as_text[digit])
                    for char in digit:
                        if char_dict[char] - 1 == 0:
                            del char_dict[char]
                        else:
                            char_dict[char] -= 1
        return "".join([str(i) for i in result])


class Solution:
    def originalDigits(self, s: str) -> str:
        count = defaultdict(int)
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        out = {}
        out["0"] = count["z"]
        out["2"] = count["w"]
        out["4"] = count["u"]
        out["6"] = count["x"]
        out["8"] = count["g"]

        # letter h is present only in three and eight
        out["3"] = count["h"] - out["8"]
        # letter f is present only in five and four
        out["5"] = count["f"] - out["4"]
        # letter s is only in seven and six
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)


if __name__ == '__main__':
    test_data = "owoztneoer"

    result = SolutionToSlow().originalDigits(test_data)
    assert result == "012"

    test_data = "fviefuro"
    result = SolutionToSlow().originalDigits(test_data)
    assert result == "45"