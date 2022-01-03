class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.window.pop(0)
            self.window.append(val)
        else:
            self.window.append(val)
        return sum(self.window) / min(len(self.window), self.size)


if __name__ == "__main__":
    test = [1, 10, 3, 5]
    m = MovingAverage(3)
    for t in test:
        result = m.next(t)
        print(result)
