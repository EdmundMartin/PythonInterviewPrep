from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mapping = {}

        for idx, item in enumerate(arr):
            if item in mapping:
                mapping[item].add(idx)
            else:
                mapping[item] = {idx}
        results = []
        for key, value in mapping.items():
            if len(value) > 1:
                continue
            results.append((list(value)[0], key))
        if k <= len(results):
            results = sorted(results)
            return results[k-1][1]
        return ""
