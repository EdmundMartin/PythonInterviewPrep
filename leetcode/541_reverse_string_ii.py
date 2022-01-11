class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        as_list = list(s)
        for i in range(0, len(as_list), 2 * k):
            as_list[i : i + k] = reversed(as_list[i : i + k])
        return "".join(as_list)
