class Solution:
    def countVowelStrings(self, n: int) -> int:
        k = 5
        acc = {}
        
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                if i == 1 or j == 1:
                    acc[(i, j)] = i
                else:
                    acc[(i, j)] = acc[(i - 1, j)] + acc[(i, j - 1)]
            
        return acc[(k, n)]
