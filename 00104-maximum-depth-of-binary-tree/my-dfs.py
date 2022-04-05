class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        
        s = []
        if root:
            s.append((root, 1))
            
        while(s):
            curr, level = s.pop()
            if not curr.left and not curr.right:
                maximum = max(level, maximum)
            
            if curr.left:
                s.append((curr.left, level + 1))
            
            if curr.right:
                s.append((curr.right, level + 1))
                 
        return maximum
