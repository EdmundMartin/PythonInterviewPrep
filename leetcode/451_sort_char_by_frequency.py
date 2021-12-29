import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        mapping = {}
        for char in s:
            if char in mapping:
                mapping[char] += 1
            else:
                mapping[char] = 1
        heap = []
        for key, value in mapping.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        result = ""
        while heap:
            value, char = heapq.heappop(heap)
            to_append = abs(value) * char
            result += to_append
        return result


if __name__ == '__main__':
    result = Solution().frequencySort("tree")
    print(result)