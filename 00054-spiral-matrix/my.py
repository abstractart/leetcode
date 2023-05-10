class Solution:
    def spiralOrder(self, matrix):
        return self.helper(matrix, 0, len(matrix), 0, len(matrix[0]), [])


    def helper(self, matrix, start_m, m, start_n, n, acc):
        if start_m >= m or start_n >= n:
            return acc

        for j in range(start_n, n):
            acc.append(matrix[start_m][j])


        for i in range(start_m + 1, m):
            acc.append(matrix[i][n - 1])

        if m - 1 > start_m:
          for j in reversed(range(start_n, n - 1)):
              acc.append(matrix[m - 1][j])

        if n - 1 > start_n:
          for i in reversed(range(start_m + 1, m - 1)):
              acc.append(matrix[i][start_n])

        return self.helper(matrix, start_m + 1, m - 1, start_n + 1, n - 1, acc)
