class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        pairs = set()
        
        for e in self.elements(root):
            s = k - e
            if s in pairs: return True
            
            pairs.add(e)
        
        return False
    
    def elements(self, root: Optional[TreeNode]):
        if not root: return
        
        yield from self.elements(root.left)
        yield root.val
        yield from self.elements(root.right)
