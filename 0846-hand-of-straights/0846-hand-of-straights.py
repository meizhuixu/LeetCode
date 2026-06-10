class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        hashmap = Counter(hand)
        for card in hand:
            # pruning
            if hashmap[card] == 0:
                continue
            
            start = card
            while hashmap[start - 1] > 0:
                start -= 1
            
            while start <= card:
                count = hashmap[start]
                if count > 0:
                    for i in range(start, start + groupSize):
                        if hashmap[i] < count:
                            return False
                        hashmap[i] -= count
                start += 1

        return True