class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        acc = []
        
        stack = []
        curr = root
        while(curr or stack):
            while(curr):
                acc.append(curr.val)
                
                stack.append(curr)
                curr = curr.left

            if stack:
                curr = stack.pop().right
        
        return acc
