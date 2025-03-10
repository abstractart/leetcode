from queue import SimpleQueue

class MyStack:

    def __init__(self):
        self.first = SimpleQueue()
        self.second = SimpleQueue()
        
    def push(self, x: int) -> None:
        self.first.put(x)
       
    def pop(self) -> int:
        while(self.first.qsize() > 1):            
            self.second.put(self.first.get())
        
        val = self.first.get()
        
        self.second, self.first = self.first, self.second
        return val
        
    def top(self) -> int:
        while(self.first.qsize() > 1):
            self.second.put(self.first.get())

        val = self.first.get()
        self.second.put(val)
        
        self.second, self.first = self.first, self.second
        
        return val
        
    def empty(self) -> bool:
        return self.first.qsize() == 0
