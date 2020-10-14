class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        stack = []
        if root: stack.append([root.left, root.right])
        
        while(len(stack) > 0):
            left, right = stack.pop()
            if not left and not right: continue
            
            if left and right and left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([right.left, left.right])
            else:
                return False
        
        return True
