class Solution:
    def mergeTwoLists(self, list1, list2):
        result = ListNode(0)
        self.helper(list1, list2, result)
        
        return result.next


    def helper(self, list1, list2, tail):
        if not list1 or not list2:
            tail.next = list1 or list2
            return
        
        if list1.val < list2.val:
            tail.next = list1
            return self.helper(list1.next, list2, list1)
        else:
            tail.next = list2
            return self.helper(list1, list2.next, list2)
