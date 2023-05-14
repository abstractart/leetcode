from collections import deque

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        indexes = deque()
        
        for i in range(len(nums)):
            if nums[i] == val:
                n -= 1
                indexes.append(i)
            elif len(indexes) > 0:
                nums[indexes.popleft()] = nums[i]
                indexes.append(i)

        return n
