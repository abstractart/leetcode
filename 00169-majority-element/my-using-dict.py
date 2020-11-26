class Solution:
    def majorityElement(self, nums):
      threshold = len(nums) // 2
      counts = dict()
      
      for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > (len(nums) // 2):
          return num
