class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        target_idx = k - 1

        while l <= r:
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            gt, lt, i = l, r, l

            while i <= lt:
                if nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt -= 1
                else:
                    i += 1

            if gt <= k - 1 <= lt:
                return pivot
            elif k - 1 < gt:
                r = gt - 1
            elif k - 1 > lt:
                l = lt + 1
        
        return