class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        res = []
        if n < 4:
            return res

        nums.sort()
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c, d = b + 1, n - 1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c + 1] == nums[c]:
                            c += 1
                        while c < d and nums[d - 1] == nums[d]:
                            d -= 1
                        c += 1
                        d -= 1

        return res
        