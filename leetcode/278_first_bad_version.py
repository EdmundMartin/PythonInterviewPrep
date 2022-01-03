

def isBadVersion(version) -> bool:
    if version >= 1:
        return True
    return False


def binary_search(array_size: int):
    left = 1
    right = array_size
    while left < right:
        middle = left + (right - left) // 2
        if isBadVersion(middle):
            right = middle
        else:
            left = middle + 1
    return left


class Solution:
    def firstBadVersion(self, n):
        return binary_search(n)


if __name__ == '__main__':
    res = Solution().firstBadVersion(3)
    print(res)