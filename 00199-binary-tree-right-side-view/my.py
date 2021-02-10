class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        nodes = []
        if root: nodes = [root]
            
        while(len(nodes) > 0):            
            result.append(nodes[-1].val)
            
            newNodes = []
            for node in nodes:
                if node.left: newNodes.append(node.left)
                if node.right: newNodes.append(node.right)
                    
            nodes = newNodes
        
        return result
