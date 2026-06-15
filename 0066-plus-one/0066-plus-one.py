class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            new = carry + digits[i]
            res.append(new % 10)
            carry = new // 10

        if carry:
            res.append(carry)

        return res[::-1]
        