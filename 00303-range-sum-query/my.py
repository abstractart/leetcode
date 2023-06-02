class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = sum(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        size = right - left + 1

        if size > len(self.nums) // 2:
            return self.s - self.sumRangeInternal(0, left - 1) - self.sumRangeInternal(right + 1, len(self.nums) - 1)
        else:
            return self.sumRangeInternal(left, right)

    
    def sumRangeInternal(self, left, right) -> int:
        s = 0
        for i in range(left, right + 1):
            s += self.nums[i]

        return s
