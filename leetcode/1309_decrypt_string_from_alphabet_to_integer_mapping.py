from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {}
        for idx, char in enumerate(ascii_lowercase):
            mapping[str(idx + 1)] = char

        idx = 0
        result = ""

        while idx < len(s) - 2:
            if s[idx + 2] == "#":
                result += mapping[s[idx : idx + 2]]
                idx += 3
            else:
                result += mapping[s[idx]]
                idx += 1
        if idx == len(s) - 2:
            result += mapping[s[-2]]
            result += mapping[s[-1]]
        elif idx == len(s) - 1:
            result += mapping[s[-1]]
        return result


if __name__ == "__main__":
    result = Solution().freqAlphabets("10#11#12")
    print(result)
