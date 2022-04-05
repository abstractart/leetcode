class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        acc = []
        
        stack = []
        curr = root
        while(stack or curr):
            while(curr):
                stack.append(curr)
                curr = curr.left
            
            if stack:
                curr = stack.pop()
                acc.append(curr.val)
                curr = curr.right
        
        return acc
