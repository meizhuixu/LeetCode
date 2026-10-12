class Solution:
    def trap(self, height: list[int]) -> int:
        # decreasing stack, store index
        stack = []
        res = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    res += (min(h, height[stack[-1]]) - bottom) * (i - stack[-1] - 1)
            stack.append(i)

        return res
        