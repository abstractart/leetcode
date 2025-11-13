from queue import SimpleQueue

class MyStack:
    def __init__(self):
        self.q = SimpleQueue()
        
    def push(self, x: int) -> None:
        l = self.q.qsize()
        
        self.q.put(x)
        
        for _ in range(l):
            self.q.put(self.q.get())
               
    def pop(self) -> int:
        return self.q.get()
        
    def top(self) -> int:
        val = self.q.get()
        self.push(val)
        return val
        
    def empty(self) -> bool:
        return self.q.qsize() == 0
