class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.isSubtreeRec(s, t)
    
    def isSubtreeRec(self, s, t, flag = False):
        if s is None and t is None: return True
        if s and t:
            if s.val == t.val:    
                result = self.isSubtreeRec(s.left, t.left, True) and self.isSubtreeRec(s.right, t.right, True)
                
                if result: return True
                
            if not flag:
                return self.isSubtreeRec(s.left, t) or self.isSubtreeRec(s.right, t)
        return False
