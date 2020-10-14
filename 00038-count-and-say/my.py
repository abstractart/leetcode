class Solution:
    def countAndSay(self, n):
        s = "1"
        
        for i in range(2, n + 1):
            cache = ""
            prev  = s[0] 
            count = 1
            
            # start with 1 because prev is s[0]
            for i in range(1, len(s)):
                if s[i] != prev: # counting is over, time to say
                    cache += "{}{}".format(count, prev)
                    count = 1
                else:
                    count += 1

                prev = s[i]
            cache += "{}{}".format(count, prev)
            s = cache
            
        return s
