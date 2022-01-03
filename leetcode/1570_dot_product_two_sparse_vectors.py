from typing import List


def process_sparse_vector(nums: List[int]):
    result = {}
    for idx, num in enumerate(nums):
        if num != 0:
            result[idx] = num
    return result


# Slow but amazing memory usage
# Runtime: 2560 ms, faster than 7.46% of Python3 online submissions for Dot Product of Two Sparse Vectors.
# Memory Usage: 17.6 MB, less than 99.73% of Python3 online submissions for Dot Product of Two Sparse Vectors.
class SparseVector:
    def __init__(self, nums: List[int]):
        self.len = len(nums)
        self.vector_hash_map = process_sparse_vector(nums)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        total = 0
        for idx in range(self.len):
            first = self.vector_hash_map.get(idx)
            if not first:
                continue
            second = vec.vector_hash_map.get(idx)
            if not second:
                continue
            total += first * second
        return total
