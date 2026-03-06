class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        # calculate each colomn, smaller of left and right tall bars
        # update the max_left and max_right
        # max_left(bottleneck) < max_right: max_left & cur -> difference
        # pointers move inward
        # time: O(n)
        # space: O(1)
        # max_left = 0, max_right = 1
        
        # height = [2, 1, 2]
        #             l                       r 
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0
        
        # iterate through the array
        while l <= r:
            if max_left < max_right:
                # height of water is determined by max_left
                max_left = max(max_left, height[l])
                res += max_left - height[l]
                l += 1
            else:
                # height of water is determined by max_right
                max_right = max(max_right, height[r])
                res += max_right - height[r]
                r -= 1
                
        return res