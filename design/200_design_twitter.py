#Approach: Use a dictionary to store the tweets of each user and a set to store the users that each user follows.
#When a user posts a tweet, add it to their list of tweets with a timestamp.
#When getting the news feed, use a min-heap to keep track of the most recent tweets from the users that the user follows, including themselves. 
#Pop the top 10 tweets from the heap and return their tweet IDs. 
#When a user follows or unfollows another user, update the set of followed users accordingly.

import heapq

class Twitter:
 
    def __init__(self):
        self.time = 0
        self.tweets = {}   # userId -> [(time, tweetId)]
        self.following = {}  # userId -> set of followed users

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):

        # User always follows themselves
        self.following.setdefault(userId, set()).add(userId)

        heap = []

        # Add the most recent tweet from each followed user
        for followee in self.following[userId]:
            if followee in self.tweets:
                i = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][i]
                heapq.heappush(
                    heap, (-time, tweetId, followee, i)
                )

        result = []

        while heap and len(result) < 10:
            neg_time, tweetId, followee, i = heapq.heappop(heap)
            result.append(tweetId)

            # Add the next older tweet from this user
            if i > 0:
                i -= 1
                time, tweetId = self.tweets[followee][i]
                heapq.heappush(
                    heap, (-time, tweetId, followee, i)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
    

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)