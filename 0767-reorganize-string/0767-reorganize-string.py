class Solution:
    def reorganizeString(self, s: str) -> str:
        # Counter
        # max-heap (freq, chr)
        #  s = 'aaab'
        #  a: 2, b: 0
        #  aba -> ''
        # a: 1, b: 0
        # new = 'ababa'
        # time: O(nlog26)  O(n)
        # space: O(26*26)  O(1)

        hashmap = Counter(s)  # {'a': 3, 'b': 2}
        pq = []
        for chr, freq in hashmap.items():
            heapq.heappush(pq, (-freq, chr)) # [(-1, 'a')]

        res = []
        temp = None
        while pq:
            freq, chr= heapq.heappop(pq) # (-1, 'b')
            res.append(chr)  # res = ['abab']
            freq += 1  # 0
            if temp:
                heapq.heappush(pq, temp)  

            if freq < 0:
                temp = (freq, chr)
            else:
                temp = None

        if len(res) == len(s):
            return ''.join(res)
        else:
            return ''




        