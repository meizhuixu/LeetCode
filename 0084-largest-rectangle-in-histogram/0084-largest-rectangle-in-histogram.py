class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights.insert(0, 0)
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                cur = stack.pop()
                if stack:
                    res = max(res, heights[cur] * (i - stack[-1] - 1))

            stack.append(i)

        return res
        