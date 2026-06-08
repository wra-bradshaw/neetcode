from dataclasses import dataclass, field
import heapq

@dataclass
class Tweet: 
    id: int
    time: int

    # Defines a min-heap relationship (oldest timestamp at the top)
    def __lt__(self, other: "Tweet") -> bool:
        return self.time < other.time

@dataclass
class User:
    id: int
    tweets: list[Tweet] = field(default_factory=list)
    following: set[int] = field(default_factory=set)

    def __post_init__(self):
        # A user automatically follows themselves
        self.following.add(self.id)

class Twitter:
    def __init__(self):
        self.time = 0
        self.id_to_users: dict[int, User] = {}
    
    def _get_or_create_user(self, userId: int) -> User:
        if userId not in self.id_to_users:
            self.id_to_users[userId] = User(userId)
        return self.id_to_users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._get_or_create_user(userId)
        user.tweets.append(Tweet(tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.id_to_users:
            return []

        user = self.id_to_users[userId]
        heap: list[Tweet] = []

        for followee_id in user.following:
            # Fix: Use .get() to prevent KeyError if the followee doesn't exist yet
            followee = self.id_to_users.get(followee_id)
            if not followee:
                continue
            
            # Optimization: Only look at the last 10 tweets (they are pre-sorted)
            for tweet in followee.tweets[-10:]:
                if len(heap) < 10:
                    heapq.heappush(heap, tweet)
                elif tweet.time > heap[0].time:
                    heapq.heappushpop(heap, tweet)
        
        # Sort descending to get newest tweets first
        heap.sort(reverse=True)
        return [tweet.id for tweet in heap]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self._get_or_create_user(followerId).following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Prevent unfollowing oneself
        if followerId == followeeId:
            return
        
        user = self.id_to_users.get(followerId)
        if user and followeeId in user.following:
            user.following.remove(followeeId)