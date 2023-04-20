class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        currNodes = []

        if root:
            currNodes.extend([(0, root)])


        while(currNodes):
            nextNodes = []
            result = max(result, currNodes[-1][0] - currNodes[0][0] + 1)

            for i, currNode in currNodes:
                if not currNode:
                    nextNodes.append((i * 2, None))
                    nextNodes.append((i  * 2 + 1, None))
                    continue
                
                if currNode.left and currNode.right:
                    nextNodes.append((i * 2, currNode.left))
                    nextNodes.append((i  * 2 + 1, currNode.right))
                    i += 2
                    continue

                if currNode.left:
                    nextNodes.append((i  * 2, currNode.left))
                if currNode.right:
                    nextNodes.append((i  * 2 + 1, currNode.right))
            currNodes = nextNodes

        
        return result
