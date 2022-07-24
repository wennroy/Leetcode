
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        from collections import defaultdict
        from sortedcontainers import SortedDict, SortedList
        self.record = defaultdict(SortedDict)
        self.food_record = {}
        n = len(foods)
        for i in range(n):
            if not ratings[i] in self.record[cuisines[i]].keys():
                self.record[cuisines[i]][ratings[i]] = SortedList()

            self.record[cuisines[i]][ratings[i]].add(foods[i])
            self.food_record[foods[i]] = [cuisines[i], ratings[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        from sortedcontainers import SortedDict, SortedList
        pos = self.food_record[food]
        self.record[pos[0]][pos[1]].remove(food)
        if not self.record[pos[0]][pos[1]]:
            self.record[pos[0]].pop(pos[1])
        if not newRating in self.record[pos[0]]:
            self.record[pos[0]][newRating] = SortedList()
        self.food_record[food] = [pos[0], newRating]
        self.record[pos[0]][newRating].add(food)

    def highestRated(self, cuisine: str) -> str:
        tmp = self.record[cuisine][self.record[cuisine].keys()[-1]]
        if tmp:
            return tmp[0]
        else:
            return None

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)