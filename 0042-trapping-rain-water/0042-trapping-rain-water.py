class Solution:
    def trap(self, height: List[int]) -> int:
        # initialize an empty stack to store the indices of the bars
        stack = []
        # and a variable res to accumulate the total amount of water trapped
        res = 0

        # iterate through the array
        for i in range(len(height)):
            # if the current bar is taller than the stack top, we've found a right boundary
            while stack and height[i] > height[stack[-1]]:
                # the bottom of the valley
                cur = stack.pop()
                # If the stack is not empty, the new stack top is our left boundary
                if stack:
                    # calculate the trapped water for this horizontal layer.
                    # the bounded height is the distance between the shorter of the two boundaries and the floor/the height is determined by the shorter of the two boundaries minus our floor
                    # the width is the distance between the boundaries
                    res += (min(height[stack[-1]], height[i]) - height[cur]) * (i - stack[-1] - 1)
            # maintain a strictly decreasing stack
            stack.append(i)

        return res
        