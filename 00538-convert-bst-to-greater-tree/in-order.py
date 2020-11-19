class Solution(object):
    def convertBST(self, root):
        s = 0
        for node in self.inOrder(root):
            node.val += s
            s = node.val
        
        return root

    def inOrder(self, root):
        if not root: return

        yield from self.inOrder(root.right)
        yield(root)
        yield from self.inOrder(root.left)
