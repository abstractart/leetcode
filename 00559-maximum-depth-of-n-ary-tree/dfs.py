class Solution:
    def maxDepth(self, root: 'Node') -> int:        
        s = []
        result = 0
        
        if root: s.append((root, 1))
        
        while(len(s) > 0):
            node, depth = s.pop()    
            
            if len(node.children) > 0:
                for child in node.children:
                    s.append((child, depth + 1))
            else:
                result = max(depth, result)       
        
        return result
