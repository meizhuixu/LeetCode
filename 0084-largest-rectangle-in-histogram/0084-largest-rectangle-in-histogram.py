class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = []
        res = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                cur = stack.pop()
                if stack:
                    res = max(res, heights[cur] * (i - stack[-1] - 1))

            stack.append(i)

        return res

        