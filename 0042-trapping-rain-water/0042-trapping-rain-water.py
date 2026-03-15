class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                if stack:
                    res += (min(height[i], height[stack[-1]]) - height[cur]) * (i - stack[-1] - 1)

            stack.append(i)

        return res

        