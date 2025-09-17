from typing import List
from heapq import heappop, heappush
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {foods[i]:[-ratings[i],cuisines[i]] for i in range(len(foods))}
        self.cuisines = {c:[] for c in set(cuisines)}
        for i in range(len(foods)):
            heappush(self.cuisines[cuisines[i]], (-ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food][0] = -newRating
        heappush(self.cuisines[self.foods[food][1]], (-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisines[cuisine][0][0] != self.foods[self.cuisines[cuisine][0][1]][0]:
            heappop(self.cuisines[cuisine])
        return self.cuisines[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
cuisines = ["korean","japanese","japanese","greek","japanese","korean"]
ratings = [9,12,8,15,14,7]
obj = FoodRatings(foods, cuisines, ratings)
print(obj.highestRated("korean"))
print(obj.highestRated("japanese"))
obj.changeRating("sushi",16)
print(obj.highestRated("japanese"))
obj.changeRating("ramen",16)
print(obj.highestRated("japanese"))
obj.changeRating("ramen",16)
print(obj.highestRated("japanese"))