class SmallestInfiniteSet:

    def __init__(self):
        self.popped = set()

    def popSmallest(self) -> int:
        i = 1

        while(True):
            if i not in self.popped:
                self.popped.add(i)
                return i
            else:
                i += 1
        

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)
