class Twitter:

    def __init__(self):
        self.time = 0
        self.t_map = defaultdict(list)
        self.f_map = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t_map[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.f_map[userId].add(userId)

        pq = []
        for u in self.f_map[userId]:
            if u in self.t_map:
                idx = len(self.t_map[u]) - 1
                time, tId = self.t_map[u][idx]
                heapq.heappush(pq, (time, tId, u, idx))

        res = []
        while pq and len(res) < 10:
            time, tId, uId, idx = heapq.heappop(pq)
            res.append(tId)

            if idx > 0:
                new_time, new_tId = self.t_map[uId][idx - 1]
                heapq.heappush(pq, (new_time, new_tId, uId, idx - 1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.f_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f_map[followerId]:
            self.f_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)