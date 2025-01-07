vowels = {'a', 'e', 'i', 'o', 'u'}

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p = self.prefixSum(words)
    
        result = []
        for l, r in queries:
            if l == 0:
                count = p[r]
            else:
                count = p[r] - p[l - 1]
            result.append(count)
        
        return result
            

    
    def prefixSum(self, words):
        r = []
        l = 0
        for w in words:
            if self.isVowelString(w):
                l += 1
            r.append(l)

        return r


    def isVowelString(self, s):
        return s[0] in vowels and s[-1] in vowels
