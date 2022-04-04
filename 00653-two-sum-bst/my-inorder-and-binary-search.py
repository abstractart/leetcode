class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        for node in self.inOrder(root):
            complement = self.find(root, k - node.val)
            
            if complement and complement != node:
                return True
        
        return False
        
    def inOrder(self, root):
        if not root:
            return
        
        yield from self.inOrder(root.left)
        yield root
        yield from self.inOrder(root.right)
    
    
    def find(self, root, k):
        if not root:
            return None
        
        if k == root.val:
            return root
        
        if k < root.val:
            return self.valueExists(root.left, k)
        else:
            return self.valueExists(root.right, k)
