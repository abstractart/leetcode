class Solution:
    def subarraySum(self, nums, k: int) -> int:
        counter = {}
        acc = 0
        
        prefix = []
        for num in nums:
            acc += num
            prefix.append(acc)
            
            if acc not in counter:
                counter[acc] = 0
            
            counter[acc] += 1
        
        count = 0
        while(prefix):            
            v = prefix.pop()
            
            counter[v] -= 1
            if v == k:
                count += 1
            if v - k in counter and counter[v - k] > 0:
                count += counter[v - k]
                    
        return count
