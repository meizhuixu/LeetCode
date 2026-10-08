class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # edge case: empty str
        if not s:
            return True
        if len(s) > len(t):
            return False

        # s = "abc"
        #        p
        # t = "ahbgdc"
        #           p
        # time  O(n)  space O(1)

        p1 = p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                if p1 == len(s):
                    return True 
            p2 += 1

        return False
            




        
        