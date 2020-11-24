# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        
        stack = []
        if root: stack.append(root)
                
        while(len(stack) > 0):
            curr = stack.pop()
            count += 1
                
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
            
        return count
