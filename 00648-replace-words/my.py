class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = self.buildTrie(dictionary)
        
        result = []
        
        for word in sentence.split():
            root = self.search(word, trie)
            if root:
                result.append(root)
            else:
                result.append(word)

        return " ".join(result)
        
    def buildTrie(self, dictionary):
        trie = {}

        for word in dictionary:
            self.insertWord(word, trie)
        
        return trie
    
    def insertWord(self, word, trie):
        curr = trie
        for i in range(len(word)):
            if word[i] not in curr:
                curr[word[i]] = {}
            curr = curr[word[i]] 

        curr['.'] = word

    def search(self, word, trie):
        curr = trie
        for i in range(len(word)):
            if '.' in curr:
                return curr['.']      
            
            if word[i] not in curr:
                return None
            
            curr = curr[word[i]]           
