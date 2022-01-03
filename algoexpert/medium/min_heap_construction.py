from typing import List


class MinHeap:
    def __init__(self, array: List[int]):
        self.heap = self.build_heap(array)

    def build_heap(self, array: List[int]):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = (
                current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            )
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_swap = child_two_idx
            else:
                idx_swap = child_one_idx
            if heap[idx_swap] < heap[current_idx]:
                self.swap(current_idx, idx_swap, self.heap)
                current_idx = idx_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i: int, j: int, heap: List[int]) -> None:
        heap[i], heap[j] = heap[j], heap[i]
