from heapq import heappop, heappush
from typing import List
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        #  movie: [(price,shop)]
        self.movies = defaultdict(list)
        # (shop,movie): price
        self.available = {}
        # (shop,movie)
        self.rented = set()

        for shop,movie,price in entries:
            self.available[(shop,movie)] = price
            self.movies[movie].append((price,shop))
        for movie in self.movies:
            self.movies[movie].sort()

    def search(self, movie: int) -> List[int]:
        # return cheapest 5 shops with movie unrented
        # tie break based on >index
        res = []
        for _, shop in self.movies.get(movie,[]):
            if (shop,movie) not in self.rented:
                res.append(shop)
            if len(res) == 5:
                break
        return res


    def rent(self, shop: int, movie: int) -> None:
        # rent unrented movie from shop
        self.rented.add((shop,movie))

    def drop(self, shop: int, movie: int) -> None:
        # returns a rented movie to shop
        self.rented.discard((shop,movie))

    def report(self) -> List[List[int]]:
        # return cheapest 5 rented movies (can be of the same movie)
        res = []
        for shop,movie in self.rented:
            price = self.available[(shop,movie)]
            res.append((price,shop,movie))
        res.sort()
        return [[shop,movie] for _,shop,movie in res[:5]]
        

# Your MovieRentingSystem object will be instantiated and called as such:

obj = MovieRentingSystem(3, [[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]])
param_1 = obj.search(1)
obj.rent(0,1)
obj.rent(1,2)
print(obj.report())
obj.drop(1,2)
print(obj.search(2))