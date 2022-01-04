class MRUQueue:
    def __init__(self, n: int):
        self.values = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        real_idx = k - 1
        value = self.values.pop(real_idx)
        self.values.append(value)
        return value


if __name__ == "__main__":
    queue = MRUQueue(8)
