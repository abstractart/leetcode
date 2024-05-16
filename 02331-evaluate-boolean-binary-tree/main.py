class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val < 2:
            return root.val == 1
        
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)

        if root.val == 2:
            return l or r
        
        return l and r
