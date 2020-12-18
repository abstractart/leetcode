class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.index = 0
        self.nestedList = nestedList
        self.iterator = None
        
    
    def next(self) -> int:
        if self.nestedList[self.index].isInteger():
            val = self.nestedList[self.index].getInteger()
            self.index += 1
            return val

        return self.iterator.next()

    
    def hasNext(self) -> bool:
        if self.index >= len(self.nestedList): return False
        if self.nestedList[self.index].isInteger(): return True
   
        if not self.iterator:
            self.iterator = NestedIterator(self.nestedList[self.index].getList())
        
        if not self.iterator.hasNext():
            self.iterator = None
            self.index += 1
            return self.hasNext()
        else:
            return True
