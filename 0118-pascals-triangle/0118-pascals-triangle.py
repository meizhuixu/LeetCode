class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(1, numRows + 1):
            row = [None for _ in range(i)]
            row[0] = row[-1] = 1

            for j in range(1, i - 1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]

            triangle.append(row)

        return triangle

        