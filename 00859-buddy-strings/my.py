class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        indexes = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indexes.append(i)
            
            if len(indexes) > 2:
                return False
        
        if not indexes:
            return len(set(s)) < len(s) 
        if len(indexes) == 1:
            return False
        
        i, j = indexes.pop(), indexes.pop()
        
        return s[i] == goal[j] and goal[i] == s[j]
