class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        
        self.nextPermutation(digits)

        np = int("".join(map(str, digits)))
        
        if abs(np) < 2**31 and np != 2**31 - 1 and np > n:
            return np
        
        return - 1

    
    def nextPermutation(self, nums):
        i = len(nums) - 2
        
        while(i >= 0 and nums[i + 1] <= nums[i]):
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            
            while(j >= 0 and nums[j] <= nums[i]):
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            
        self.reverse(nums, i + 1)
        
    
    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        
        while(i < j):
            nums[i], nums[j]= nums[j], nums[i]
            
            i += 1
            j -= 1
