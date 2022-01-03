from typing import List


class CustomOrder:
    def __init__(self, ordering_str: str):
        self.order = self._build_order(ordering_str)

    def _build_order(self, ordering_string: str):
        mapping = {}
        for idx, val in enumerate(ordering_string):
            mapping[val] = idx
        return mapping

    def get_value(self, char: str):
        return self.order.get(char, float("inf"))


class Solution:
    def quicksort(self, array: List[str], order):
        if len(array) == 0:
            return []
        if len(array) == 1:
            return array
        pivot = array[0]
        smaller = []
        partition = [pivot]
        larger = []
        pivot_val = order.get_value(pivot)
        for i in range(1, len(array)):
            if order.get_value(array[i]) == pivot_val:
                partition.append(array[i])
            elif order.get_value(array[i]) > pivot_val:
                larger.append(array[i])
            else:
                smaller.append(array[i])
        return (
            self.quicksort(smaller, order) + partition + self.quicksort(larger, order)
        )

    def customSortString(self, order: str, s: str) -> str:
        order = CustomOrder(order)
        result = self.quicksort(list(s), order)
        return "".join(result)
