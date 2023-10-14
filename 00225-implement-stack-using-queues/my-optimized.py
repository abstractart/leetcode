from queue import SimpleQueue

class MyStack:

    def __init__(self):
        self.first = SimpleQueue()
        self.second = SimpleQueue()
        
    def push(self, x: int) -> None:
        self.second.put(x)
        
        while(self.first.qsize() > 0):
            self.second.put(self.first.get())
        
        self.first, self.second = self.second, self.first
       
    def pop(self) -> int:
        return self.first.get()
        
    def top(self) -> int:
        val = self.first.get()
        self.push(val)
        return val
        
    def empty(self) -> bool:
        return self.first.qsize() == 0
