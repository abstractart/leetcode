class BSTIterator:
    def __init__(self, root: TreeNode):
        self.curr = root
        self.stack = []
        

    def next(self) -> int:
        if self.curr is not None:  
            self.stack.append(self.curr) 

            self.curr = self.curr.left
            return self.next()
        elif(self.stack): 
            curr = self.stack.pop() 
            val = curr.val
            self.curr = curr.right  

            return val

    def hasNext(self) -> bool:
        return self.stack or self.curr
