class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        acc = []
        
        self.helper(root, acc)
        
        return acc
    
    def helper(self, root, acc):
        if not root:
            return
        
        self.helper(root.left, acc)
        acc.append(root.val)
        self.helper(root.right, acc)
