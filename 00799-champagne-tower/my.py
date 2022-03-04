class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        matr = []
        matr.append([poured])
            
        while(len(matr) < query_row + 1):
            row = [0] * (len(matr[-1]) + 1)
            
            for i in range(len(matr[-1])):
                v = (matr[-1][i] - 1)  / 2
                
                row[i] += max(v, 0)
                row[i + 1] += max(v, 0)
                
            matr.append(row)
            
        return min(matr[query_row][query_glass], 1)
