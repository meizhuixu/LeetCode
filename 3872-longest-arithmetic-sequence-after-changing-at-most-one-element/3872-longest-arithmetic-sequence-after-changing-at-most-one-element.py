class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        # 直接拿 m 作为基准，彻底告别原数组长度 n
        m = len(nums) - 1
        diff = [nums[i + 1] - nums[i] for i in range(m)]

        left = [1] * m
        right = [1] * m
        
        # 1. 预处理左右连续相等的长度
        for i in range(1, m):
            if diff[i] == diff[i-1]:
                left[i] = left[i-1] + 1

        for i in range(m - 2, -1, -1):
            if diff[i] == diff[i+1]:
                right[i] = right[i+1] + 1

        # 基础最大长度
        max_len = max(left)

        # 2. 修改原数组首尾的边界情况
        max_len = max(max_len, 1 + right[1], left[m - 2] + 1)

        # 3. 核心遍历：修改原数组中间元素，恰好对应 diff 索引 1 到 m-1 的影响范围
        for i in range(1, m):
            # 单向延伸
            if i >= 2:
                max_len = max(max_len, left[i-2] + 1)
            
            if i + 1 < m:
                max_len = max(max_len, right[i+1] + 1)

            # 平分差值，尝试双向搭桥
            sum_d = diff[i-1] + diff[i]
            if sum_d % 2 == 0:
                d = sum_d // 2
                curr_len = 2 
                
                if i >= 2 and diff[i-2] == d:
                    curr_len += left[i-2]
                
                if i + 1 < m and diff[i+1] == d:
                    curr_len += right[i+1]
                
                max_len = max(max_len, curr_len)

        return max_len + 1