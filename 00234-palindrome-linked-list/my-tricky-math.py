class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        number = 0
        reverse = 0
        
        curr = head
        curr_pow = 1
        
        while(curr):
            number = number * 10 + curr.val
            reverse = curr.val * curr_pow + reverse
            
            curr = curr.next
            curr_pow *= 10
            
        return reverse == number
        
