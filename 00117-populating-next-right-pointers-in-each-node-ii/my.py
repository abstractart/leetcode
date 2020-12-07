# Copy-paste 116 solution
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        nodes = []
        if root: self.levelTraversal([root], nodes)
        
        for i in range(len(nodes)):
            for j in range(len(nodes[i]) - 1):
                nodes[i][j].next = nodes[i][j + 1]
        
        return root
                
    
    def levelTraversal(self, nodes, acc):        
        childs = []
        for n in nodes:
            if n.left: childs.append(n.left)
            if n.right: childs.append(n.right)
        
        if len(childs) == 0: return acc
        
        acc.append(childs)
        
        return self.levelTraversal(childs, acc)
