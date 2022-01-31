class MinStack:
    def __init__(self):
        self.arr = []
        self.min_arr = [float('+inf')]

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.min_arr.append(min(val, self.min_arr[-1]))

    def pop(self) -> None:
        self.min_arr.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
