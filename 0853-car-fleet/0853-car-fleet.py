class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        # time = reach target
        # position: decrease
        # position = [10,8,0,5,3]
        # [10, 8, 5, 3, 0]
        # [1, 1,| 7, 3, | 12]

        
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        stack = []
        res = 0
        for p, s in pairs:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                res += 1
                stack.append(time)

        return res
        
        