class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
