class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        stack = []
        result = []
        
        if root:
            stack.append((root, []))
            
        while(len(stack) > 0):
            
            curr, path = stack.pop()
            if curr.left is None and curr.right is None:
                path.append(str(curr.val))
                result.append("->".join(path))
            else:
                if curr.left: stack.append((curr.left, list(path) + [str(curr.val)]))
                if curr.right: stack.append((curr.right, list(path) + [str(curr.val)]))
        
        return result
