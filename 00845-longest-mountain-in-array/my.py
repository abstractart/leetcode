class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        index = 1
        maximum = 0
        
        while(index < len(arr) - 1):
            l = index
            r = index
            
            while(l - 1 >= 0 and arr[l - 1] < arr[l]):
                l -= 1
            while(r + 1 < len(arr) and arr[r + 1] < arr[r]):
                r += 1
            
            if l != index and r != index:
                maximum = max(maximum, r - l + 1)
            
            index = r + 1
            
        return maximum
