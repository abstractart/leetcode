class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1 = []        
        acc = []
        
        if root:
            s1.append(root)
            
        while(s1):
            curr = s1.pop()
            
            acc.append(curr.val)
            
            if curr.left:
                s1.append(curr.left)
            
            if curr.right:
                s1.append(curr.right)
            
        
        acc.reverse()
        return acc
