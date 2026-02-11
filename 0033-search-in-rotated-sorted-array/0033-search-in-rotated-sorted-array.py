class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #  nums = [0,1,2,4,5,6,7]
        #  nums = [4,5,6,7,0,1,2]
        #          l        m  r
        #  nums = [4,5,6,7,8,9,0,1,2]
        #                  ml      r
        
        # time: O(logn) n = len(nums)
        # space: O(1)
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1   
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1
        