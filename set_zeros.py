class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """         
        m = len(matrix)
        n = len(matrix[0])
        row_index = set()
        column_index = set()
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    row_index.add(i)
                    column_index.add(j)
                    
        for i in range(0, m):
            for j in range(0, n):
                if i in row_index or j in column_index:
                    matrix[i][j] = 0
