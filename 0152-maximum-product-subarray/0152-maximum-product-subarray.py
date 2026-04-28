class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums = [-2,0,-1]
        # max_product: 1,   -2, 0, 0
        # min_product: 1,   -2, 0, -1
        # res: 
        # nums = [2,3,-2,4]
        # max_product: 1,  2, 6, -2, 4
        # min_product: 1,  2, 3, -12, -48

        min_product = max_product = 1
        res = float('-inf')

        for num in nums:
            temp = max_product
            max_product = max(num, num * temp, num * min_product)
            min_product = min(num, num * temp, num * min_product)
            res = max(res, max_product)

        return res
        

        