class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        stack = []
        
        if root:
            stack.append(root)
            
        while(len(stack)):
            curr = stack.pop()
            
            result.append(curr.val)
            
            for child in reversed(curr.children):
                stack.append(child)
        
        
        return result
