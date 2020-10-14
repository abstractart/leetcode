class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        return self.helper(root.left, root.right)
        

    def helper(self, left, right):
        if not left and not right: return True
        
        if left and right and left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(right.left, left.right)
        
        return False
