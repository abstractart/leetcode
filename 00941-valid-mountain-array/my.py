class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top = 0
        
        for i in range(len(arr)):
            if arr[top] < arr[i]: top = i
        
        if top not in range(1, len(arr) - 1): return False
        
        left = top - 1
        right = top + 1
        while(left >= 0):
            if arr[left] >= arr[left + 1]: return False
            
            left -= 1
        
        while(right <= len(arr) - 1):
            if arr[right] >= arr[right - 1]: return False
            
            right += 1
        
        return True
