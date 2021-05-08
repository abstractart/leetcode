class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.helper(1, n + 1, k)
    
    def helper(self, start, end, k):
        if k == 0: return [[]]

        result = []
        
        for i in range(start, end):
            temp = self.helper(i + 1, end, k - 1)
            
            for t in temp:
                t.append(i)
            
            result.extend(temp)
        
        return result
