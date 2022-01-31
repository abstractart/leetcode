class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for i in range(len(s)):
            s_i, t_i = s[i], t[i]
            
            if s_i not in s_t:
                s_t[s_i] = t_i
            
            if t_i not in t_s:
                t_s[t_i] = s_i
                
            if s_t[s_i] != t_i or t_s[t_i] != s_i:
                return False

        return True
