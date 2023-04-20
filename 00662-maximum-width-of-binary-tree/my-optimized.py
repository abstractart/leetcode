class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        currNodes = []

        if root:
            currNodes.extend([(0, root)])

        while(currNodes):
            result = max(result, currNodes[-1][0] - currNodes[0][0] + 1)
            
            nextNodes = []

            for i, currNode in currNodes:
                if currNode.left:
                    nextNodes.append((i  * 2, currNode.left))
                if currNode.right:
                    nextNodes.append((i  * 2 + 1, currNode.right))
            
            currNodes = nextNodes
        
        return result
    
