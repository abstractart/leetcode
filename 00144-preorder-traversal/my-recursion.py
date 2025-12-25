class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        acc = []
        self.helper(root, acc)
        return acc
    
    def helper(self, root, acc):
        if not root:
            return
        
        acc.append(root.val)
        self.helper(root.left, acc)
        self.helper(root.right, acc)
