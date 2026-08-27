#Approach: Use a dictionary to map each food to its cuisine and rating. 
#For each cuisine, maintain a max-heap (using negative ratings) to efficiently retrieve the highest-rated food. 
# When changing a food's rating, update the rating in the dictionary and push the new rating into the heap. 
# When retrieving the highest-rated food for a cuisine, pop from the heap until the top food's rating 
# matches the current rating in the dictionary, ensuring that stale ratings are removed.

import heapq

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating

            if cuisine not in self.cuisine_heap:
                self.cuisine_heap[cuisine] = []

            heapq.heappush(
                self.cuisine_heap[cuisine],
                (-rating, food)
            )

    def changeRating(self, food, newRating):
        self.food_to_rating[food] = newRating

        cuisine = self.food_to_cuisine[food]

        # Push new version into heap
        heapq.heappush(
            self.cuisine_heap[cuisine],
            (-newRating, food)
        )

    def highestRated(self, cuisine):
        heap = self.cuisine_heap[cuisine]

        # Remove stale ratings
        while True:
            neg_rating, food = heap[0]
            rating = -neg_rating

            if self.food_to_rating[food] == rating:
                return food

            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)