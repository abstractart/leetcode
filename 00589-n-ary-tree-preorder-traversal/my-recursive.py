class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self.helper(root, [])
    
    def helper(self, root, acc):
        if not root: return acc
        
        acc.append(root.val)
        
        for child in root.children:
            self.helper(child, acc)
        
        return acc
