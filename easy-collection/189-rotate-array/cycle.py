class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        count = start = 0
        while(count < n):
            curr, prev = start, nums[start]
            print(nums)
            while(True):
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                print(nums)
                curr = next_idx
                count += 1
                
                if start == curr:
                    break
            
            start += 1
 
