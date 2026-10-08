class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        def findInsert(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []
        for _, h in envelopes:
            insert = findInsert(tails, h)
            if insert == len(tails):
                tails.append(h)
            else:
                tails[insert] = h

        return len(tails)