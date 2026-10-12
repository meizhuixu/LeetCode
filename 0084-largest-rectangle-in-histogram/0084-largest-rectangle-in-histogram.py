class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # increasing stack, save idx
        # edge case: len(heights) == 1 ; heights[0] == 0
        # first & last rectangle
        heights.insert(0, 0)
        heights.append(0)
        stack = []
        res = 0

        for idx, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                peak = heights[stack.pop()]
                res = max(res, peak * (idx - stack[-1] - 1))
            stack.append(idx)

        return res
