class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        m = [[None for x in range(n)] for y in range(n)]
        
        count = 0
        for i in range(0, len(nums) - 2):
            if self.isArithmetic(nums, i, i + 2):
                m[i][i + 2] = nums[i + 1] - nums[i]
                count += 1
        
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if m[i][j - 1] is None: continue
                
                if nums[j] - nums[j - 1] == m[i][j - 1]:
                    m[i][j] = m[i][j - 1]
                    count += 1
        
        return count
    
    
    def isArithmetic(self, nums, low, high):
        if len(nums) < 3: return False
        
        diff = nums[low + 1] - nums[low]
        
        for i in range(low + 1, high + 1):
            if nums[i] - nums[i - 1] != diff:
                return False
            
        return True
