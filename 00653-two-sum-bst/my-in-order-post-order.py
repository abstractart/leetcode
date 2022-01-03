class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return
        
        inOrder, postOrder = self.inOrder(root), self.postOrder(root)
        left, right  = next(inOrder), next(postOrder)

        while(left != right):
            if left.val + right.val < k:
                left = next(inOrder)
            elif left.val + right.val > k: 
                right = next(postOrder)
            else:
                return True

        return False
        
    
    def inOrder(self, root: Optional[TreeNode]):
        if not root: return
        
        yield from self.inOrder(root.left)
        yield root
        yield from self.inOrder(root.right)

    def postOrder(self, root: Optional[TreeNode]):
        if not root: return
        
        yield from self.postOrder(root.right)
        yield root
        yield from self.postOrder(root.left)
