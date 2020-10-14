class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        return self.isSymmetricTrees(root.left, root.right)
        

    def isSymmetricTrees(self, left, right):
        if not left and not right: return True
        
        if left and right:
            if left.val != right.val: return False 
            
            return self.isSymmetricTrees(left.left, right.right) and self.isSymmetricTrees(left.right, right.left) 
        
        return False
