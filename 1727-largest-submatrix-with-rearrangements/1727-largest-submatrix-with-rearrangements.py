class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            if i > 0:
                for j in range(n):
                    if matrix[i][j] != 0:
                        matrix[i][j] += matrix[i - 1][j]

            sorted_row = sorted(matrix[i], reverse=True)
            for j in range(n):
                res = max(res, sorted_row[j] * (j + 1))

        return res
        