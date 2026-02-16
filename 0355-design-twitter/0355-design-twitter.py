class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # {followerId: {followeeId, ..}}
        self.tweets = defaultdict(list) # {userId: [(time, tweetId), ..]}
        self.time = 0 # tweet  time += 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # add foloweeId + userId into one list
        users = [user for user in self.following[userId]] + [userId]
        
        pq = []
        for user in users:
            for time, tweet in self.tweets[user][-10:]:
                heapq.heappush(pq, (time, tweet))
                if len(pq) > 10:
                    heapq.heappop(pq)
                    
        res = []
        while pq:
            _, tweet = heapq.heappop(pq)
            res.append(tweet)
        return res[::-1]
                 

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)