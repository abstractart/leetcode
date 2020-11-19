from queue import Queue
class Solution:
    def maxDepth(self, root: 'Node') -> int:        
        q = Queue()
        result = 0
        
        if root: q.put((root, 1))
        
        while(q.qsize() > 0):
            node, depth = q.get()            
            for child in node.children:
                q.put((child, depth + 1))
            
            result = depth       
        return result
