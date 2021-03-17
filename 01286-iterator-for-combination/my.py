class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.current = None
        self.limit = len(characters) - 1
        self.length = combinationLength
        self.chars = characters

    def next(self) -> str:
        if not self.current:
            self.current = list(range(self.length))
    
        else:
            curr_limit = self.limit
            i = self.length - 1
    
            while(i >= 0):
                if self.current[i] < curr_limit:
                    self.current[i] += 1
                    break
                else:
                    curr_limit = self.current[i] - 1
                    i -= 1

            for index in range(i + 1, len(self.current)):
                self.current[index] = self.current[index - 1] + 1
            
        return "".join(map(lambda n: self.chars[n], self.current))
        
    def hasNext(self) -> bool:
        return self.current != list(range(self.limit + 1 - self.length, self.limit + 1))
