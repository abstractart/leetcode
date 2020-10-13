class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lastNonZero = 0
        curr = 0
        
        while(curr < len(nums)):
            print("{} {}".format(lastNonZero, curr))
            
            if nums[curr] != 0:
                nums[lastNonZero], nums[curr] = nums[curr], nums[lastNonZero]
                lastNonZero += 1
            curr += 1
            print(nums)
                
