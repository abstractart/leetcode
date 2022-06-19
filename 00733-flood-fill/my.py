from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        rows, columns = range(m), range(n)

        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        old_color = image[sr][sc]
        
        if old_color == color:
            return image
    
        queue = deque()
        queue.append((sr, sc))
        while(len(queue)):
            curr_sr, curr_sc = queue.popleft()
            
            image[curr_sr][curr_sc] = color
            for i, j in moves:
                
                if curr_sr + i in rows and curr_sc + j in columns:
                    if image[curr_sr + i][curr_sc + j] == old_color:
                        queue.append((curr_sr + i, curr_sc + j))
                    
        return image
