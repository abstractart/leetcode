class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursive(n, n, [], [])
    
    
    def recursive(self, o, c, curr, acc):
        if o == c and o == 0:
            acc.append("".join(curr))
            return acc
        
        if o > 0:
            curr.append("(")
            self.recursive(o - 1, c, curr, acc)
            curr.pop()
        if c > o:
            curr.append(")")
            self.recursive(o, c - 1, curr, acc)
            curr.pop()
        
        return acc
