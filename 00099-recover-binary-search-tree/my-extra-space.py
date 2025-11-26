class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        values = []
        
        for n in self.inOrder(root):
            values.append(n)
        
        first = None
        second = None
        for i in range(len(values) - 1):
            if values[i].val > values[i + 1].val:
                if not first:
                    first = values[i]
                second = values[i + 1]

                    
                    
        tmp = first.val
        first.val = second.val
        second.val = tmp
    
    def inOrder(self, root):
        if not root: return

        yield from self.inOrder(root.left)
        yield(root)
        yield from self.inOrder(root.right)
        
