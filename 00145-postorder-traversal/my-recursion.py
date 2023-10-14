class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        acc = []
        self.helper(root, acc)
        return acc
    
    def helper(self, root, acc):
        if not root:
            return
        
        self.helper(root.left, acc)
        self.helper(root.right, acc)
        acc.append(root.val)
