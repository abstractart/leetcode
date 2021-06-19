class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:        
        stack = [root]
        
        while(len(stack) > 0):
            curr = stack.pop()
            if not curr: continue
            
            curr.left, curr.right = curr.right, curr.left
            
            stack.append(curr.left)
            stack.append(curr.right)
        
        return root
