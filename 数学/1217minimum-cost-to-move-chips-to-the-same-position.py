class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count, even_count = 0, 0
        for num in position:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return min(odd_count, even_count)