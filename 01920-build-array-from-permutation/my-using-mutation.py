class Solution:
    def buildArray(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        for i in range(n):
            nums.append(nums[nums[i]])
            
        nums.reverse()
        for _ in range(n):
            nums.pop()
        
        nums.reverse() 
        return nums
