class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = matrix
        for i in range(m):
            sum_row = 0
            for j in range(n):
                sum_row += self.prefix[i][j]
                self.prefix[i][j] = sum_row

        for j in range(n):
            sum_col = 0
            for i in range(m):
                sum_col += self.prefix[i][j]
                self.prefix[i][j] = sum_col

        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s1 = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        s2 = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        s3 = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return (self.prefix[row2][col2] - s1 - s2 + s3)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)