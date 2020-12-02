class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True

        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root):
        if not root: return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1
