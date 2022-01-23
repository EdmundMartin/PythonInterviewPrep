from string import ascii_lowercase


class CylicArray:

    def __init__(self):
        self.array = list(ascii_lowercase)

    def steps_forward(self, last, target):
        steps = 0
        current = self.array.index(last)
        while self.array[current] != target:
            current += 1
            if current >= len(self.array):
                current = 0
            steps += 1
        return steps

    def steps_backwards(self, last, target):
        steps = 0
        current = self.array.index(last)
        while self.array[current] != target:
            current -= 1
            if current < 0:
                current = len(self.array) - 1
            steps += 1
        return steps


class Solution:
    def minTimeToType(self, word: str) -> int:
        cyclic_array = CylicArray()
        last = 'a'
        total_time = 0
        for char in word:
            steps_forward = cyclic_array.steps_forward(last, char)
            steps_back = cyclic_array.steps_backwards(last, char)
            total_time += min(steps_forward, steps_back)
            last = char
        return total_time + len(word)


if __name__ == '__main__':
    result = Solution().minTimeToType("bza")
    print(result)