class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        count_s1 = Counter(s1)  # s1 = 'ab', count_s1 = {a: 1, b: 1}
        count_s2 = defaultdict(int) # sliding window
        meet = l = 0 
        # matched char in two dictionaries, count == len(count_s1) -> True
        # after iterate through -> False
        
        for r in range(len(s2)):
            # add s2[r] into dict
            cur = s2[r]
            count_s2[cur] += 1
            if count_s2[cur] == count_s1[cur]:
                meet += 1
                
            # check left pointer
            if r - l + 1 > len(s1):
                drop = s2[l]
                if count_s2[drop] == count_s1[drop]:
                    meet -= 1
                count_s2[drop] -= 1

                l += 1
                
            # check permutation
            if meet == len(count_s1):
                return True
                
        return False
                
        
                
            
                
            
        
        