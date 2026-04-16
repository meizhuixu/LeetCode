class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.friends = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.friends[userId]
        users.add(userId)

        pq = []
        for u in users:
            if self.tweets[u]:
                t, tId = self.tweets[u][-1]
                heapq.heappush(pq, (-t, tId, u, 1))

        res = []
        while pq and len(res) < 10:
            neg_t, tId, u, count = heapq.heappop(pq)
            res.append(tId)

            if count < len(self.tweets[u]):
                next_t, next_tId = self.tweets[u][-(count + 1)]
                heapq.heappush(pq, (-next_t, next_tId, u, count + 1))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.friends[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.friends[followerId]:
            self.friends[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)