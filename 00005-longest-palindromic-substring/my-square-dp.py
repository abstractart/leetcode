class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            
        r = range(0, 1)
        
        for i in reversed(range(n - 1)):
            for j in reversed(range(i + 1, n)):
                if i == j:
                    continue

                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                
                if dp[i][j]:                    
                    new = range(i, j + 1)
                    if len(new) > len(r):
                        r = new
        return s[r.start:r.stop]
