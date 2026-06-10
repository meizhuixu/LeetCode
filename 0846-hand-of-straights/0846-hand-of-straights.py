class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check its mod -> False
        # sort
        # 1, 2, 2, 3, 3, 4, 6, 7, 8
        # Counter
        # {1: 1, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1}

        if len(hand) % groupSize != 0:
            return False

        hashmap = Counter(hand)
        for num in hand: # 4
            start = num  
            while hashmap[start - 1] > 0: # find start
                start -= 1  # 1

            while start in hashmap and start <= num:
                while hashmap[start] > 0:
                    temp = start
                    for _ in range(groupSize):
                        if hashmap[temp] > 0:
                            hashmap[temp] -= 1
                            temp += 1
                        else:
                            return False
                start += 1

        
        return True
