from typing import List


class Solution:

    def quicksort(self, array):
        if len(array) == 0:
            return []
        if len(array) == 1:
            return array
        pivot = array[0]
        smaller = []
        partition = [pivot]
        larger = []
        for i in range(1, len(array)):
            if array[i][1] > pivot[1]:
                larger.append(array[i])
            elif array[i][1] < pivot[1]:
                smaller.append(array[i])
            else:
                partition.append(array[i])
        return self.quicksort(smaller) + partition + self.quicksort(larger)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        results = [(k, v) for k, v in counter.items()]
        results = self.quicksort(results)
        output = []
        for i in range(k):
            output.append(results.pop()[0])
        return output


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    Solution().topKFrequent(nums, k)