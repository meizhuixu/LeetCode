class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left, right: 0-index
        # increasing queue: big -> small
        # step1: put nums[r] into queue tail
        # step2: check sliding window is within k
        # move l to right -> check queue[0] < l -> pop queue[0]
        # step3: window == k -> add maximum(queue[0]) into res array
        
        # Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        #                            l   r 
        # queue = [] store index, not num
        # time: O(n)
        # space: O(k)
        
        queue = deque()
        res = []
        l = 0
        
        for r in range(len(nums)):
            # step1: add nums[r] into window
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            
            # step2: check sliding window <= k
            if r - l + 1 > k:
                l += 1
                if queue[0] < l:
                    queue.popleft()
                    
            # step3: get maximum
            if r - l + 1 == k:
                res.append(nums[queue[0]])
                
        return res
                
        