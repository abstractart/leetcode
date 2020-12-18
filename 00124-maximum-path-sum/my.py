class Solution:
    def __init__(self):
        self.max_value = float('-inf')
    
    def maxPathSum(self, root):
        self.maxPathSumRec(root)
        return self.max_value

    def maxPathSumRec(self, root):
        if root is None: return 0
        
        l = self.maxPathSumRec(root.left)
        if l < 0: l = 0 
            
        r = self.maxPathSumRec(root.right)
        if r < 0: r = 0
            
        self.max_value = max(self.max_value, root.val + l + r)
        
        return max(root.val + l, root.val + r)
