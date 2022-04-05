from queue import SimpleQueue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        
        q = SimpleQueue()
        if root:
            q.put((root, 1))
            
        while(q.qsize() > 0):
            curr, level = q.get()
            maximum = max(level, maximum)
            
            if curr.left:
                q.put((curr.left, level + 1))
            
            if curr.right:
                q.put((curr.right, level + 1))
                
        return maximum
