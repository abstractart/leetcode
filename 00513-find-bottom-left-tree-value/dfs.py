class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxLevel = 0
        maxNode = root
        
        for currNode, currLevel in self.lnr(root, 0):
            if currLevel > maxLevel:
                maxLevel, maxNode = currLevel, currNode
        
        return maxNode.val
    
    def lnr(self, root, level):
        if not root:
            return
        
        yield from self.lnr(root.left, level + 1)
        yield (root, level)
        yield from self.lnr(root.right, level + 1)
