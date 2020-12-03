class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:        
        result = TreeNode(0)
        tail = result
        
        for node in self.inOrder(root):
            tail.right = TreeNode(node.val)
            tail = tail.right
        
        return result.right
        
    def inOrder(self, node):
        if not node: return

        yield from self.inOrder(node.left)
        yield(node)
        yield from self.inOrder(node.right)
