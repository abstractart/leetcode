class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        stack = []
        
        if root:
            stack.append((root, targetSum))
        
        while(stack):
            curr_node, curr_sum = stack.pop()
            
            if self.isLeaf(curr_node) and curr_sum == curr_node.val:
                return True
            
            if curr_node.left:
                stack.append((curr_node.left, curr_sum - curr_node.val))

            if curr_node.right:
                stack.append((curr_node.right, curr_sum - curr_node.val))
        
        return False
    
    def isLeaf(self, node):
        return node.left is None and node.right is None
