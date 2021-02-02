class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root: return None
        
        if root.val >= low and root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            
            return root
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
