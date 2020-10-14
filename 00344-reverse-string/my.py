class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, finish = 0, len(s) - 1
        
        while(start < finish):
            s[start], s[finish] = s[finish], s[start]
            
            start += 1
            finish -= 1
        
