class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        return self.recoverFromPreorderRec(S, 0, [])
        
    def recoverFromPreorderRec(self, S, curr_level, parents):        
        node = TreeNode(self.parseValue(S))
        
        if len(parents) > 0:
            parent = self.findParent(parents, curr_level)
            if parent.left:
                parent.right = node
            else:
                parent.left = node
        
        parents.append((node, curr_level))
        next_level = self.nextLevel(S)
        
        if "-" in S:
            S = S[S.index('-') + next_level:]
            self.recoverFromPreorderRec(S, next_level, parents)
        
        return node
    
    
    def nextLevel(self, S):
        if "-" not in S: return 0
        
        count = 0
        for i in range(S.index('-'), len(S)):
            if S[i] != "-": break
            
            count += 1
        return count

    
    def parseValue(self, S):
        if "-" in S:
            return int(S[0:S.index('-')])
        
        return int(S)

    def findParent(self, parents, level):
        while(parents[-1][1] != level - 1):
            parents.pop()
                
        return parents[-1][0]
