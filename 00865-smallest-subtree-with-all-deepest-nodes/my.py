class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None
        
        stack = [(root, 1, [])]
        deepest_nodes = []
        tree_level = self.levelOfTree(root)
        
        while(len(stack) > 0):
            node, level, parents = stack.pop()
            
            if node.left is None and node.right is None and level == tree_level:
                deepest_nodes.append((node, parents + [node]))
                
            if node.left: stack.append((node.left, level + 1, parents + [node]))
            if node.right: stack.append((node.right, level + 1, parents + [node]))


        for i in reversed(range(tree_level)):
            parents = set()
            
            for d in deepest_nodes:
                parents.add(d[1][i])
            
            if len(parents) == 1: return parents.pop()
            if len(parents) == 0: return root
                
            
    
    def levelOfTree(self, root):
        if not root: return 0
        
        return max(self.levelOfTree(root.left), self.levelOfTree(root.right)) + 1
