class Solution:
    def isPalindrome(self, head):
        l = self.length(head)
        if l <= 1: return True

        middle = l // 2
        left = head

        element = middle + 1
        if l % 2 == 1: element + 1


        right = self.nth(head, element)
        right = self.reverse(right)

        while(left and right):
            if left.val != right.val: return False
            left = left.next
            right = right.next

        return True

  
    def length(self, head):
        l = 0
        while(head):
            l += 1
            head = head.next

        return l
  
    def reverse(self, head):
        target = None

        while(head):
            newHead = head.next

            head.next = target
            target = head

            head = newHead

        return target


    def nth(self, head, n):
        while(n > 1):
            head = head.next
            n -= 1

        return head
        
