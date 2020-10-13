class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        slow = 0 # Last non zero
        fast = slow + 1 # Current
        
        while(fast < len(nums)):
            print("{} {}".format(slow, fast))
            if nums[slow] == 0: # if we have zero before number - swap
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                else:
                    fast += 1
                
            else:
                slow += 1
                fast += 1
        
