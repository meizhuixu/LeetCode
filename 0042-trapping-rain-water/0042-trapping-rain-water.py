class Solution:
    def trap(self, height: List[int]) -> int:
        # keep track of the maximum height seen so far from both the left and the right sides
        max_left = max_right = 0
        # placing pointers at both ends
        # initialize l at the beginning and r at the end of the array
        l, r = 0, len(height) - 1
        res = 0

        while l <= r:
            # The water level at any point is determined by the shorter of the two tall bars on its left and right
            # process the side that has the smaller maximum
            if max_left < max_right:
                # If we are moving the left pointer, we first update max_left
                max_left = max(max_left, height[l])
                # If the current bar is shorter than max_left, the difference is the trapped water at this specific column
                res += max_left - height[l]
                # moving inwards / moving the pointer towards the center
                l += 1
            else:
                max_right = max(max_right, height[r])
                res += max_right - height[r]
                r -= 1

        return res
        # It only takes O(n) time because we traverse the array once, and O(1) space since we only use a few variables



        