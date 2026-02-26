class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for num in nums:
            if num < pivot:
                right.append(num)
            elif num > pivot:
                left.append(num)
            else:
                mid.append(num)
        
        if k <= len(left):
            return self.findKthLargest(left, k)
        if k > len(left) + len(mid):
            return self.findKthLargest(right, k - len(left) - len(mid))

        return pivot