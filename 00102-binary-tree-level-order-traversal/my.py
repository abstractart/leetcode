class Solution:
    def levelOrder(self, root):
        acc = []
    
        if root: self.recursive([root], acc)
        
        return acc
        
        
    def recursive(self, nodes, acc):
        values = []
        next_nodes = []
        
        for node in nodes:                
            values.append(node.val)
            
            if node.left: next_nodes.append(node.left)
            if node.right: next_nodes.append(node.right)
        
        if len(values) > 0: acc.append(values)
        if len(next_nodes) > 0: self.recursive(next_nodes, acc)
        
        
        
