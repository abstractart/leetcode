class Solution:
    def __init__(self, head: ListNode):
        self.values = []
        
        curr = head
        while(curr):
            self.values.append(curr.val)
            
            curr = curr.next
 
    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values) - 1)]
