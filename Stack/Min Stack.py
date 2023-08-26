class MinStack:
    # 56ms 93%
    # 20.3mb 64%
    def __init__(self):
        self.list = []
        self.min = []

    def push(self, val: int) -> None:
        self.list.append(val)
        self.min.append(min(val, self.min[-1] if min else val))

    def pop(self) -> None:
        self.list.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min[-1]
