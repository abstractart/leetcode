class Trie:

    def __init__(self):
        self.children = dict()
        self.endings = dict()

    def insert(self, word: str) -> None:
        if len(word) == 0: return

        if word[0] not in self.children:
            self.children[word[0]] = Trie()

        if not self.endings.get(word[0], False):
            self.endings[word[0]] = len(word) == 1
        
        
        return self.children[word[0]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        if len(word) == 0: return True
        
        curr = self
        while(len(word) > 1):
            if not curr: return False
            if word[0] not in curr.children: return False
            
            curr = curr.children[word[0]]
            word = word[1:]
            
        if curr and word[0] in curr.children: return curr.endings[word[0]]
        
        return False
        
        

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0: return True
        
        curr = self
        while(len(prefix) > 0):
            if not curr: return False
            if prefix[0] not in curr.children: return False
            
            curr = curr.children[prefix[0]]
            prefix = prefix[1:]
        
        return True
