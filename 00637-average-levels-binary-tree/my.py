from queue import SimpleQueue

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = SimpleQueue()
        
        if root:
            q.put(root)
            
        while(q.qsize()):
            levelSize = q.qsize()
            
            s = 0
            for _ in range(levelSize):
                node = q.get()
                
                s += node.val
                
                if node.left:
                    q.put(node.left)
                
                if node.right:
                    q.put(node.right)
                
            result.append(s / levelSize)
                
        return result
