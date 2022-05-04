class Solution:
    def countVowelStrings(self, n: int) -> int:
        size = 5
        state = list(range(1, size + 1))
        
        for _ in range(n - 1):
            for i in range(1, size):
                state[i] += state[i - 1]
        
        return state[-1]
