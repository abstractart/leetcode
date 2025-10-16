class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return [node.val for node in self.preOrder(root)]

    
    def preOrder(self, node):
        if not node: return

        yield(node)
        for child in node.children:
            yield from self.preOrder(child) 
