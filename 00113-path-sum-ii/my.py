class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        stack = []
        result = []
        if root:
            stack.append((root, 0, []))
            
        while(stack):
            curr_node, curr_sum, path = stack.pop()
            
            if self.isLeaf(curr_node) and curr_sum + curr_node.val == targetSum:
                result.append(path + [curr_node.val])
            
            if curr_node.left:
                stack.append((curr_node.left, curr_sum + curr_node.val, path + [curr_node.val]))
            
            if curr_node.right:
                stack.append((curr_node.right, curr_sum + curr_node.val, path + [curr_node.val]))
        return result
    
    
    def isLeaf(self, node):
        return node.left is None and node.right is None
