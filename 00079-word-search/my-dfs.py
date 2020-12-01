class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j): return True
    
        
    def search(self, board, word, i, j):
        stack = []
        stack.append((i, j, 0, set()))
        index = 0        
        while(len(stack) > 0):
            i, j, index, visited = stack.pop()
            if board[i][j] != word[index]: continue
            
            visited.add((i, j))                
            
            if index + 1 == len(word): return True
    
            if i - 1 in range(len(board)) and (i - 1, j) not in visited:
                stack.append(
                    (i - 1, j, index + 1, set(visited))
                )
            if i + 1 in range(len(board)) and (i + 1, j) not in visited:
                stack.append((i + 1, j, index + 1, set(visited)))
            
            if j - 1 in range(len(board[0])) and (i, j - 1) not in visited:
                stack.append((i, j - 1, index + 1, set(visited)))
            if j + 1 in range(len(board[0])) and (i, j + 1) not in visited:
                stack.append((i, j + 1, index + 1, set(visited)))
                
        return False
