class LRUCache:
    def __init__(self, capacity: int):
        self.d = dict()
        self.c = capacity
        self.l = LinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        
        node = self.d[key]
        
        self.l.remove(node)
        self.l.appendToHead(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            n = Node(key, value)
            
            self.l.appendToHead(n)
            self.d[key] = self.l.getHead()
            
            if self.l.size > self.c:
                n = self.l.getTail()
                
                self.l.remove(n)
                del self.d[n.key]
                
        else:
            n = self.d[key]
            n.val = value
            
            self.l.remove(n)
            self.l.appendToHead(n)
                        
        
        
        
class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail
        
        self.size = 0

    def appendToHead(self, n):
        left = self.head
        right = self.head.next

        left.next = n
        n.prev = left

        right.prev = n
        n.next = right
            
        self.size += 1
    
    def remove(self, n):
        self.size -= 1     
        
        left = n.prev
        right = n.next

        left.next = right
        right.prev = left
        
        n.prev = None
        n.next = None

    def getHead(self):
        if self.head.next != self.tail:
            return self.head.next
    
    def getTail(self):
        if self.tail.prev != self.head:
            return self.tail.prev
   
