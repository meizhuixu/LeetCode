class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # time O(n*n) space O(1)
        # numRows = 5
        res = [[1]]  

        for i in range(numRows - 1): # 3
            curr = [1]  # 1, 4, 6, 4, 1
            for j in range(i):
                curr.append(prev[j] + prev[j+1])
            curr.append(1)
            res.append(curr)
            prev = curr # 1, 3, 3, 1

        return res
