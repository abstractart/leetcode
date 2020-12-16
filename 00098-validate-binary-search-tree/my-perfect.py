class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)
        
    
    def helper(self, root, l = float("-inf"), r = float("inf")):
        if not root: return True
        
        if root.val > l and root.val < r:
            return self.helper(root.left, l, root.val) and self.helper(root.right, root.val, r)
        
        return False
