from queue import SimpleQueue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = SimpleQueue()
        if root:
            q.put(root)
        
        acc = []
        while(q.qsize() > 0):
            levelValues = []
                        
            for i in range(q.qsize()):
                curr = q.get()
                
                levelValues.append(curr.val)
                
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                
            
            acc.append(levelValues)

        return acc
