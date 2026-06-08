from dataclasses import dataclass
from typing import Self
import heapq

@dataclass
class Tweet: 
    id: int
    time: int

    def __lt__(self, other: Self):
        return self.time < other.time

@dataclass
class User:
    id: int
    tweets: list[Tweet]
    following: set[int]

    def __init__(self, id: int):
        self.id = id
        self.tweets = []
        self.following = set([id])

class Twitter:
    time: int
    id_to_users: dict[int, User]

    def __init__(self):
        self.time = 0
        self.id_to_users = {}
    
    def _get_or_create_user(self, userId: int) -> User:
        if userId in self.id_to_users:
            return self.id_to_users[userId]
        else:
            new_user = User(userId)
            self.id_to_users[userId] = new_user
            return new_user

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._get_or_create_user(userId).tweets.append(Tweet(tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.id_to_users:
            return []

        user = self.id_to_users[userId]
        heap: list[Tweet] = []

        for followee_id in user.following:
            followee = self.id_to_users[followee_id]
            for tweet in followee.tweets:
                if len(heap) < 10:
                    heapq.heappush(heap, tweet)
                elif tweet.time > heap[0].time:
                    heapq.heappushpop(heap, tweet)
        
        heap.sort(reverse=True)

        return [v.id for v in heap]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self._get_or_create_user(followerId).following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self._get_or_create_user(followerId)
        if followeeId in user.following and followeeId != user.id:
            self._get_or_create_user(followerId).following.remove(followeeId)
        
